import pandas as pd
df = pd.read_csv('IMDB.csv')
result = df
result11 = df.columns
result = df.info
result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)

result1 = df["Title"]
result1 = df["Title"].tail()
result1 = df[["Title", "Year"]].head(10)
result1 = df[["Title", "Year", "DVD"]].tail(7)


result2 = df[5:][["Title", "Year", "DVD"]].head()
result2 = df[5:10][["Title", "Year", "DVD"]]
result2 = df[df["Year"] > 2000][["Title", "Year", "DVD"]].head(50)
result2 = df[(df["Year"] > 2000) & (df["Year"] <= 2015)][["Title", "Year", "DVD"]].head(10)
result2 = df[(df["imdbRating"] >= 3.0) | (df["imdbRating"] <= 9.0)][["Title", "imdbRating"]].tail(50)

print(result11)
print(result2)