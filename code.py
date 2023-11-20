import random

# Simulated sports events data
sports_events = {
    1: {"name": "Basketball - Team A vs. Team B", "odds": {"Team A": -1.5, "Team B": +2.0}},
    2: {"name": "Football - Team X vs. Team Y", "odds": {"Team X": -3, "Team Y": +3}},
    # Add more simulated events here
}

# User account data
users = {
    "user1": {"password": "pass123", "balance": 1000},
    "user2": {"password": "pass456", "balance": 1500},
    # Add more user accounts here
}

current_user = None  # Track the current user

# Function to validate user credentials
def login(username, password):
    global current_user
    if username in users and users[username]["password"] == password:
        current_user = username
        return True
    return False

# Function to display available sports events
def display_events():
    print("Available Sports Events:")
    for event_id, event_info in sports_events.items():
        print(f"{event_id}. {event_info['name']} - Odds: {event_info['odds']}")

# Function to place a bet on a sports event
def place_bet(event_id, team, amount):
    global current_user
    if current_user:
        event = sports_events.get(event_id)
        if event and team in event['odds']:
            odds = event['odds'][team]
            if amount <= users[current_user]["balance"]:
                outcome = random.choice([True, False])  # Simulate event outcome
                if outcome:
                    winnings = amount * odds
                    users[current_user]["balance"] += winnings
                    print(f"Congratulations! You won {winnings}!")
                else:
                    users[current_user]["balance"] -= amount
                    print("Sorry, you lost the bet.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid event or team.")
    else:
        print("Please login first.")

# Sample usage
username = input("Enter username: ")
password = input("Enter password: ")

if login(username, password):
    print(f"Welcome, {username}!")
    display_events()
    event_choice = int(input("Choose an event to bet on: "))
    selected_event = sports_events.get(event_choice)
    if selected_event:
        selected_team = input(f"Choose a team ({', '.join(selected_event['odds'].keys())}): ")
        bet_amount = float(input("Enter the amount to bet: "))
        place_bet(event_choice, selected_team, bet_amount)
    else:
        print("Invalid event.")
else:
    print("Invalid credentials.")
