import pandas as pd


data = pd.read_csv("nba_elo.csv")
# data.dropna(inplace=True)

column = data.columns

# print(column)
# data["team1"] = data["team1"].str.upper()
# data["team1"] = data["team1"].str.lower()
# result = data["team1"].str.upper().head(10)
# result = data.team1.str.contains('CLR').head(10)
# result = data[data.team1.str.contains('CLR')]
result = data.date.str.replace("-", "/")

print(result.head(10))

