import pandas as pd


# 1. inner join    -> siparisi olan butun musteriler gelsin
# 2. left join    -> musteriler(soldaki) gelsin siparis(sagdakiler) yoksa NaN atayarak getir
# 3. right join    -> siparisler(sagdaki) gelsin musteriler(soldaki) yoksa NaN atayarak getir
# 4. outer join    -> siparisler(sagdaki) ve musteriler(soldaki) kayitli olsun olmasin hepsini getiriyor.



"""
customers = {
    'CustomerId': [1, 2, 3, 4],
    'FirstName': ["Arafat", "Rahile", "Meryem", "Mustafa"],
    'LastName': ["Emin", "Ablimit", "Emin", "Gappar"],
}

orders = {
    'OrderId': [10, 20, 30, 40],
    'CustomerId': [1, 2, 5, 4],
    'OrderDate': ["2022-05-05", "2021-09-01", "2020-06-06", "2019-09-09"],
}

df_customers = pd.DataFrame(customers, columns=["CustomerId", "FirstName", "LastName"])
df_orders = pd.DataFrame(orders, columns=["OrderId", "CustomerId", "OrderDate"])

print(df_customers)
print(df_orders)

result = pd.merge(df_customers, df_orders, how="inner")

result = pd.merge(df_customers, df_orders, how="left")

result = pd.merge(df_customers, df_orders, how="right")

result = pd.merge(df_customers, df_orders, how="outer")
print(result)
"""





customersA = {
    'CustomerId': [1, 2, 3, 4],
    'FirstName': ["Arafat", "Rahile", "Meryem", "Mustafa"],
    'LastName': ["Emin", "Ablimit", "Emin", "Gappar"],
}

customersB = {
    'CustomerId': [4, 5, 6, 7],
    'FirstName': ["Can", "Melek", "Elif", "Mustafa"],
    'LastName': ["Bilgi", "Sayar", "Emin", "Arafat"],
}


df_customersA = pd.DataFrame(customersA, columns=["CustomerId", "FirstName", "LastName"])
df_ordersB = pd.DataFrame(customersB, columns=["CustomerId", "FirstName", "LastName"])


result = pd.concat([df_customersA, df_ordersB])
result = pd.concat([df_customersA, df_ordersB], axis=0) # Row
result = pd.concat([df_customersA, df_ordersB], axis=1) # Col
print(result)
