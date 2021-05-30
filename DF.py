import pandas as  p

data={'Name':['jai','pronce', 'gaurav', 'anuj'],
        'Height':[5.2,5.1,5.6,5.8],
        'qualification':['MSC','MA','MSC','MSC']}

df = p.DataFrame(data)
aaddress = ['delhi','banglor','noida','chennai']
df['Address']=aaddress
age=[25,26,24,27]
df['Age']=age

print(df)


# # column deletion
# # making data frame from csv file
# data = p.read_csv("file.csv", index_col="Name")

# # dropping passed column
# data.drop(["Team", "Height"], axis=1 , inplace=True)

# print(data)


# Row selection
# import pandas as pd

# # making data frame from csv file
# data = pd.read_csv("file.csv", index_col="Name")
# # retrieving row by loc method

# first=data.loc["raj"]
# second=data.loc["rahul"]
# print(first, "\n\n\n", second)



# #Row Addition
# import pandas as pd
# df = pd.read_csv("file.csv", index_col="Name")
# df.head(10)
# new_row = pd.DataFrame({'Name':'Geeta', 'Team':'Boston',
#         'Position':'PG', 'Age':33,'Height':5.3})


# df=pd.concat([new_row, df]).reset_index(drop=True)
# df.head(5)


#Row Deletion

import pandas as pd

data = pd.read_csv("file.csv", index_col="Name")
data.drop(["raj", 'rahhul'], inplace=True)
#display
data
