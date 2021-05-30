import pandas as pd

data = pd.read_csv("testfile.csv")
print(data.head)

# print age
# ages= data["Age"]
# print(ages)
# address= data["address"]
# print(address)

# print(type(data(["Age"])))
# pd.core.series.Series
# count  total age s.n
# print(data["Age"].shape)


# fetch  name and age
# name_age = data[["Name", "Age"]]
# print(name_age.head())2

# print type
# print(type(data[["Name", "Age"]]))


# belowag_26= data[data["Age"]<26]
# print(belowag_26)

# salaryabove = data[data["salary"]>15000]
# print(salaryabove)


# fetch value with respect to another value
# adult_name = data.loc[data["Age"]>26, ["Name","address"]]
# print(adult_name)

# interested in rows3 to 6 and column 3to 4
# d=data.iloc[3:7, 2:4]
# print(d)


# age_mean = data["Age"].mean()
# print(age_mean)

# median = data[["Age", "salary"]].median()
# print(median)


# des = data[["Age", "salary"]].describe()
# print(des)

# group = data[["salary", "Age"]].groupby("salary").mean
# print(group)

# count = data["Age"].value_counts()
# print(count)


#number of salary in each of the classes ie. count the grouping value
count = data["salary"].value_counts()
print(count)

grp_count = data.groupby("salary")["salary"].count()
print(grp_count)