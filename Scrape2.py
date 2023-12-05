import requests
from bs4 import BeautifulSoup

# Define the sportsbooks and their URLs
sportsbooks = ["Caesers", "Fanduel", "BetMGM"]
urls = ["https://www.actionnetwork.com/nfl/odds",]

# Get the data from the sportsbooks
data = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table with the NFL lines
    table = soup.find("table", {"class": "table table-bordered table-striped"})

    # Get the data from the table
    for row in table.find_all("tr"):
        # Get the team names
        team1 = row.find("th").text
        team2 = row.find("td").text

        # Get the spread, moneyline, and total
        spread = row.find("td", {"class": "spread"}).text
        moneyline = row.find("td", {"class": "moneyline"}).text
        total = row.find("td", {"class": "total"}).text

        # Add the data to the list
        data.append({
            "team1": team1,
            "team2": team2,
            "spread": spread,
            "moneyline": moneyline,
            "total": total
        })

# Display the data
print(data)