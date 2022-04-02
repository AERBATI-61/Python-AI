import pandas as pd


list = [
    ["base_of_python", 50],
    ["Mehmet", 60],
    ["Ayse", 40],
    ["Ali", 80]
]

dict = {
    "Name": ["Arafat", "Rahile", "Meryem", "Emin"],
    "Grade": [100, 90, 80, 70]
}
dict_list = [
    {
        "Name": "Rahile",
        "Grade": 100
    },
    {
        "Name": "Arafat",
        "Grade": 90
    },
    {
        "Name": "Meryem",
        "Grade": 80
    },
    {
        "Name": "Emin",
        "Grade": 99
    }
]
df1 = pd.DataFrame()
df2 = pd.DataFrame([1, 2, 3, 4, 5])
df3 = pd.DataFrame([["base_of_python", 50], ["Mehmet", 60], ["Ayse", 40], ["Ali", 80]])
df4 = pd.DataFrame(list, index=[1, 2, 3, 4], columns=['isim', 'puan'])
df5 = pd.DataFrame(dict, index=[1, 2, 3, 4])
df6 = pd.DataFrame(dict_list, index=[1, 2, 3, 4])

print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)

"""
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])
data = dict(apples=s1, orange=s2)
print(data)
df = pd.DataFrame(data)
print(df)
"""
