import pandas as pd
import numpy as np

Personeller = {
    'Calisanlar': ['Arafat', 'Rahile', 'Meryem'],
    'Departman': ['Bilgisayar Muhendisi', 'Ev Hanimi', 'Bilgisayar Muhendisi'],
    'Yas': ['27', '22', '0.10'],
    'Semt': ['Trabzon', 'istanbul', 'istanbul'],
    'Maas': [20000, 20000, 30000]
}

df = pd.DataFrame(Personeller)
# result = df
# print(df)
# result = df["Maas"].sum()
#
# result = df.groupby(["Semt", "Departman"]).groups
# result = df.groupby("Semt").groups
#
# print(result)
# semtler = df.groupby("Semt")
#
# for name, group in semtler:
#     print("-", name)
#     print(group)
#     print("")
# #
# for name, group in df.groupby("Maas"):
#     print("->", name)
#     print(group)
#     print("")

result = df.groupby("Semt").get_group("istanbul")
result = df.groupby("Maas").get_group(20000)
result = df.groupby("Departman").mean()
result = df.groupby("Departman").sum()
result = df.groupby("Departman")["Maas"].sum()
result = df.groupby("Departman")["Maas"].mean()
result = df.groupby("Semt")["Yas"].mean()
result = df.groupby("Semt")["Yas"].max()
result = df.groupby("Departman")["Yas"].min()
result = df.groupby("Semt")["Calisanlar"].count()
result = df.groupby("Departman")["Maas"].min()
result = df.groupby("Departman")["Maas"].max()["Bilgisayar Muhendisi"]
result = df.groupby("Departman")["Maas"].agg(np.mean)  # aggregration birden fazla parametre alabiliyor.
result = df.groupby("Departman")["Maas"].agg([np.sum, np.mean, np.max, np.min])
result = df.groupby("Departman")["Maas"].agg([np.sum, np.mean, np.max, np.min]).loc["Bilgisayar Muhendisi"]
result = df["Maas"].sum()
print(result)