import pandas as pd
import numpy as np

data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 60, 20, 70, 40],
    "Column3": ["abc", "bca", "adea", "cb", "dea"],
}

df = pd.DataFrame(data)
result = df
result = df["Column1"].unique()
result = df["Column2"].unique()
result = df["Column2"].value_counts()
result = df["Column2"] * 2


def kareal(x):
    return x*x

kareal2 = lambda x: x*x

result = df["Column2"].apply(kareal)
result = df["Column2"].apply(kareal2)
result = df["Column2"].apply(lambda x: x*x)
result = df["Column3"].apply(len)
df["Column4"] = df["Column3"].apply(len)
print(df)


result = df.columns
result = df.index
result = len(df.columns)
result = len(df.index)
result = df.info
result = df.sort_values("Column2")
result = df.sort_values("Column2", ascending=False) # azalan halinde siraliyor.



data2 = {
    "Ay": ["Mayis", "Haziran", "Nisan"],
    "Kategory": ["BM", "MM", "EM"],
    "Gelir": [3000, 12000, 40000]
}

df2 = pd.DataFrame(data2)
print(df2.pivot_table(index="Ay", columns="Kategory", values="Gelir"))




# print(result)