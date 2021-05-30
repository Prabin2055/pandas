import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
# print(dates)



'''
Viewing data

df.head()
df.tail()
df.index()
df.columns()
df.describe()
df.T #transposing
df.sort_index(axis=1, ascending=False)
df.sort_values(by="B)

'''

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]} )
df["grade"]=df["raw_grade"].astype("category")
print(df["grade"])