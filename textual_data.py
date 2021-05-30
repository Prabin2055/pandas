import pandas as pd

std = pd.read_csv("testfile.csv")
# print(std.head())


# A = std["Name"].str.upper()
# print(A)
# A = std["Name"].str.lower()
# print(A)
A = std["Name"].str.title()
# print(A)

B = std["Name"].str.split(",")
# print(B)

std["Surname"]=std["Name"].str.split(",").str.get(0)
# c = std['Surname']
# print(c)

D = std["Name"].str.contains("Countess")
# print(D)

E = std[std["Name"].str.contains("Countess")]
# print(E)
#output
# Empty DataFrame
# Columns: [S.N, Name, Age, Position, qualification, address, salary, contact, email, Surname]
# Index: []

std["address_short"]= std["address"].replace({"bardiya":"ktm","dang":"ktm"})
print(std["address_short"])