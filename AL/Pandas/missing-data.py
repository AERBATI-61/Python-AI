import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)
df = pd.DataFrame(data, index=['a', 'c', 'e', 'f', 'h'], columns=["Column1", "Column2", "Column3"])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
newColumn = [np.nan, 30, np.nan, 40, np.nan, 50, np.nan, 60]
df["Column4"] = newColumn


result = df
result = df.drop("Column1", axis=1)


# result = df.drop(["Column1", "Column2"], axis=1)
result = df.drop(["a", "b", "f"], axis=0)


#
# result = df.isnull()
# result = df.notnull()
result = df.isnull().sum()


# result = df["Column1"].isnull().sum()
# result = df["Column1"].isnull()
result = df[df["Column1"].notnull()]["Column4"]
print(result)
# result = df[df["Column1"].isnull()]
# result = df[df["Column1"].notnull()]
# result = df[df["Column1"].notnull()]["Column1"]
#
#
# result = df.dropna(axis=0) # axis=0 satira gore silme islemi yapar
# result = df.dropna(axis=1) # axis=1 sutun'e gore silme islemi yapar
# result = df.dropna(how="any")
# result = df.dropna(how="all")  # butun elemanlari null olan sutunu siler
# result = df.dropna(subset=["Column1", "Column4"], how="all")
#
# result = df.dropna(thresh=2)  # herhangibir satirda en az sayida normal sayi varsa silme
# result = df.dropna(thresh=1)
# result = df.dropna(thresh=4)
#
#
#
# result = df.fillna(value="No input")
# result = df.fillna(value=1)
#
#
# result = df.sum().sum()
# result = df.size
# result = df.isnull().sum()
# result = df.isnull().sum().sum()
#
#
#
# def ortalama(df):
#     toplam = df.sum().sum()
#     adet = df.size - df.isnull().sum().sum()
#     return toplam/adet
# result = df.fillna(value=ortalama(df))
# print(result)
