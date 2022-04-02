import pandas as pd
import numpy as np


data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

# print(data)
# print(df)
# print(df.columns)
# print(df.head(10))
# print(df.tail(10))
# print(df["Column1"].head())
# print(df["Column1"].tail())
# print(df[["Column1", "Column2"]].tail())
# print(df[5:15][["Column1", "Column4"]].head(3))
# print(df[5:15][["Column1", "Column2"]].tail(3))
#
# print(df > 50)
# print(df[df > 50])
# print(df[df % 2 == 0])
# print(df["Column1"] > 50)
# print(df[df["Column1"] > 50])
# print(df[df["Column1"] > 50][["Column1", "Column2"]])
# print(df[(df["Column1"] > 50) & (df["Column1"] <= 70)][["Column1", "Column2"]])
# print(df[(df["Column1"] > 50) & (df["Column2"] <= 70)][["Column1", "Column2"]])
# print(df[(df["Column1"] > 50) | (df["Column2"] > 70)])
# print(df[(df["Column1"] > 50) | (df["Column2"] > 70)][["Column1", "Column2"]])
print(df.query("Column1 > 50 & Column1 %2 == 0"))
print(df.query("Column1 > 50 & Column1 %2 == 0")[["Column1", "Column2"]])
print(df.query("Column1 > 50 | Column1 %2 == 0")[["Column1", "Column2"]])

