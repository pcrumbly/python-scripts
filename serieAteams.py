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
