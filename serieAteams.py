import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
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




# Import necessary libraries
import pandas as pd

# Loop through the teams and links in the dictionary
for team, link in teams_dict.items():
    # Send a GET request to the team's Wikipedia page
    team_response = requests.get(link)
    
    # Parse the HTML content using BeautifulSoup
    team_soup = BeautifulSoup(team_response.content, "html.parser")
    
    # Find the "infobox vcard" table for team details
    infobox_table = team_soup.find("table", class_="infobox vcard")
    
    # Initialize a dictionary to store team details
    team_details = {}
    
    # Extract team details from the infobox table
    for row in infobox_table.find_all("tr"):
        header = row.find("th")
        if header:
            key = header.text.strip()
            value = row.find("td").text.strip()
            team_details[key] = value
    
    # Find the "wikitable football-squad nogrid" table for player information
    squad_table = team_soup.find("table", class_="wikitable football-squad nogrid")
    
    # Initialize a list to store player information
    player_list = []
    
    # Extract player information from the squad table
    for row in squad_table.find_all("tr")[1:]:
        columns = row.find_all("td")
        player_name = columns[2].text.strip()
        player_position = columns[1].text.strip()
        player_age = columns[0].text.strip()
        player_list.append({"Name": player_name, "Position": player_position, "Age": player_age})
    
    # Create a DataFrame for player information
    player_df = pd.DataFrame(player_list)
    
    # Print team details and player information
    print(f"Team: {team}")
    print("Team Details:", team_details)
    print("Player Information:")
    print(player_df)
    print("\n")
