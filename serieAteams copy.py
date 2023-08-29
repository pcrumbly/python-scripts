# Import necessary libraries
import csv
import os
import pandas as pd
import requests

from bs4 import BeautifulSoup

# URL of the 2023/24 Serie A Season
url = "https://en.wikipedia.org/wiki/Serie_A#2023%E2%80%9324_season"


# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the Serie A teams
table = soup.find("table", class_="wikitable")

# Initialize an empty dictionary to store team names and links
teams_dict = {}

# Loop through each row in the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    # Find the columns (td) in the row
    columns = row.find_all("td")
    
    # Get the team name from the "Team" column
    team_name = columns[0].text.strip()
    
    # Find the link in the "Team" column
    team_link = columns[0].find("a")["href"]
    
    # Construct the full Wikipedia link
    full_link = f"https://en.wikipedia.org{team_link}"
    
    # Store the team name and link in the dictionary
    teams_dict[team_name] = full_link

# Print the dictionary with team names and links
for team, link in teams_dict.items():
    print(f"Team: {team}\nLink: {link}\n")



# Iterate through the teams_dict to scrape each team's page
for team, link in teams_dict.items():
    # Send a GET request to the team's Wikipedia page
    team_response = requests.get(link)
    
    # Parse the team's page HTML content using BeautifulSoup
    team_soup = BeautifulSoup(team_response.content, "html.parser")
    
    # Find all tables with class "wikitable football-squad nogrid"
    player_tables = team_soup.find_all("table", class_="wikitable football-squad nogrid")
    
    # List to store player information for the current team
    player_list = []
    
     # Iterate through each player table and extract player information
    for player_table in player_tables:
        for row in player_table.find_all("tr")[1:]:
            columns = row.find_all("td")
            if len(columns) >= 4:
                player_number = columns[0].text.strip()
                player_position = columns[1].text.strip()
                player_nation = columns[2].text.strip()
                player_name = columns[3].text.strip()
                
                # Slice the player's name to remove everything after "("
                player_info_start = player_name.find("(")
                if player_info_start != -1:
                    player_info = player_name[player_info_start:].strip()
                    player_name = player_name[:player_info_start].strip()
                else:
                    player_info = ""
                
                player_info = {
                    "No.": player_number,
                    "Pos.": player_position,
                    "Nation": player_nation,
                    "Player": player_name,
                    "Info": player_info
                }
                player_list.append(player_info)
    
    # Print player information for the current team
    print(f"Player list for {team}:")
    for player in player_list:
        print(player)
    print("\n")

    # Create the "squads" folder if it doesn't exist
    if not os.path.exists("squads"):
        os.makedirs("squads")

    # Prepare CSV filename
    csv_filename = f"squads/{team.lower().replace(' ', '_')}_squad.csv"
    
    # Save player information to CSV
    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["No.", "Pos.", "Nation", "Player", "Info"]
        writer = csv.writer(csv_file)

        writer.writerow(fieldnames)
        writer.writerows([player_info[field] for field in fieldnames] for player_info in player_list)

    
    print(f"Player information for {team} saved in {csv_filename}\n")