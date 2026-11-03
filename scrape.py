import pandas as pd

# 2025/26 Premier League results
url = "https://www.football-data.co.uk/mmz4281/2526/E0.csv"

df = pd.read_csv(url)

# Keep completed matches only
df = df.dropna(subset=["FTHG", "FTAG", "FTR"])

# Convert dates
df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# Create home team records
home = pd.DataFrame({
    "team_name": df["HomeTeam"],
    "opposing_team": df["AwayTeam"],
    "win_or_lose": df["FTR"].map({
        "H": "w", "D": "d", "A": "l"
    }),
    "goal_difference": df["FTHG"] - df["FTAG"],
    "date_played": df["Date"]
})

# Create away team records
away = pd.DataFrame({
    "team_name": df["AwayTeam"],
    "opposing_team": df["HomeTeam"],
    "win_or_lose": df["FTR"].map({
        "H": "l", "D": "d", "A": "w"
    }),
    "goal_difference": df["FTAG"] - df["FTHG"],
    "date_played": df["Date"]
})

# Combine both perspectives
matches = pd.concat([home, away], ignore_index=True)

# Sort by date
matches = matches.sort_values("date_played")

# Format dates
matches["date_played"] = matches["date_played"].dt.strftime("%d/%m/%Y")

# Export CSV
matches.to_csv("premier_league_2025_26_matches.csv", index=False)

print(matches)
print("Total rows:", len(matches))