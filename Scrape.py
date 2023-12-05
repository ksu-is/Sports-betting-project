import requests
from bs4 import BeautifulSoup

# URL of the Action Network NFL odds page
url = 'https://www.actionnetwork.com/nfl/odds'

# Send a GET request to the website
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the elements containing the odds data
    # Use the developer tools in your browser to inspect the HTML structure and identify the elements
    odds_data = soup.find_all('div', class_='your-odds-class')

    # Process and extract the odds data
    for data in odds_data:
        # Extract specific information from the found elements
        # Example: print(data.text) to see the text content of the found elements
        # You might need to apply additional parsing to extract the odds in the desired format
        print(data)
else:
    print("Failed to fetch data from the website.")
