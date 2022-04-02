import pandas as pd
from numpy import *
# random. randint, randn, rand


df = pd.DataFrame(random.rand(3, 3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])

print(df)
# result1 = df["Column1"]
# print(type(df["Column1"]))
# result2 = df[["Column1", "Column2"]]
# result_2 = df[["Column1", "Column2", "Column3"]]




#Secme islemi loc["row", "column] => loc["row"] => loc[":", "column"]
# iloc[0] => index'e gore secme islemi
result3 = df.loc["A"]
result_3 = df.iloc[0]
result4 = type(df.loc["A"])
result5 = df.loc[:, "Column1"]
result6 = df.loc[:, ["Column1", "Column2"]]
result7 = df.loc[:, "Column1": "Column3"]
result8 = df.loc[:, : "Column3"]
result9 = df.loc["A":"B", : "Column3"]
result10 = df.loc["A":, : "Column3"]
result11 = df.loc["A", "Column3"]
result12 = df.loc["C", "Column2"]
result13 = df.loc[["A", "C"], ["Column1", "Column3"]]


# print(result1)
# print(result2)
# print(result_2)
# print(result3)
# print(result_3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)
# print(result8)
# print(result9)
# print(result10)
# print(result11)
# print(result12)
# print(result13)



#Ekleme islemleri
df["Column4"] = pd.Series(random.rand(3), ["A", "B", "C"])
df["Column5"] = df["Column1"] + df["Column3"]
print(df)

#silme islemleri
# y koordinati 1 (yukardan asaya dogru),  x koordinati 0 (soldan saga dogru) olarak kabul edilir
sonuc1 = df.drop("Column5", axis=1)
print(sonuc1)
print(df)

sonuc2 = df.drop("Column5", axis=1, inplace=True)   #inplace=True, veya False olarak droptan donen deger gercek deger olacak
print("sonuc2: inplace = True oldugunda None deger donecek. Cunku veri gercek olarak silindi. :", sonuc2)
print(df)
