

def display_sportsbook_spreads(home_team, away_team, spreads):
    print(f"NFL Game: {home_team} vs {away_team}")
    for sportsbook, data in spreads.items():
        spread = data['spread']
        home_odds = data['home_odds']
        away_odds = data['away_odds']
        print(f"{sportsbook} Spread: {home_team} -{spread}, {away_team} +{spread}")
        print(f"{sportsbook} Home Team Odds: {home_odds}")
        print(f"{sportsbook} Away Team Odds: {away_odds}")
        print()

# Example usage
home_team = "Jacksonville Jaguars"
away_team = "Cincinnati Bengals"
spreads = {
    "Caesers": {
        "spread": 10,
        "home_odds": -110,
        "away_odds": -110
    },
    "Fanduel": {
        "spread": 10.5,
        "home_odds": -102,
        "away_odds": -120
    },
    "BetMGM": {
        "spread": 10,
        "home_odds": -110,
        "away_odds": -110
    }
}

display_sportsbook_spreads(home_team, away_team, spreads)

def display_sportsbook_moneylines(home_team, away_team, moneylines):
    print(f"NFL Game: {home_team} vs {away_team}")
    for sportsbook, odds in moneylines.items():
        home_odds = odds['home']
        away_odds = odds['away']
        print(f"{sportsbook} Moneyline: {home_team} {home_odds} | {away_team} {away_odds}")

# Example usage
home_team = "Jacksonville Jaguars"
away_team = "Cincinnati Bengals"
moneylines = {
    "Caesers": {
        "home": -600,
        "away": 430
    },
    "Fanduel": {
        "home": -560,
        "away": 420
    },
    "BetMGM": {
        "home": -500,
        "away": 375
    }
}
display_sportsbook_moneylines(home_team, away_team, moneylines)

def display_sportsbook_totals(home_team, away_team, totals):
    print(f"NFL Game: {home_team} vs {away_team}")
    for sportsbook, data in totals.items():
        total = data['total']
        over_odds = data['over_odds']
        under_odds = data['under_odds']
        print(f"{sportsbook} Total: {total}")
        print(f"{sportsbook} Over Odds: {over_odds}")
        print(f"{sportsbook} Under Odds: {under_odds}")
        print()

# Example usage
home_team = "Jacksonville Jaguars"
away_team = "Cincinnati Bengals"
totals = {
    "Caesers": {
        "total": 40.5,
        "over_odds": -110,
        "under_odds": -110
    },
    "Fanduel": {
        "total": 40.5,
        "over_odds": -110,
        "under_odds": -110
    },
    "BetMGM": {
        "total": 40.5,
        "over_odds": -110,
        "under_odds": -110
    }
}

display_sportsbook_totals(home_team, away_team, totals)