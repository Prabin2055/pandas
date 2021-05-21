# create a dataframe from lists
import pandas as p
from pandas.io.stata import precision_loss_doc
# d1=[1,2,3,4,5]
# df=p.DataFrame(d1)
# print(df)

# d2=[['raj',10],['rahul',20],['rishav',50]]
# df2=p.DataFrame(d2, columns=['Name','Age'])
# print(df2)

# Create a DataFrame from Dict of ndarrays / Lists

# data1={'Name':['simla','geeta','sita'],'Age':[22,23,24],'qualification':['bbs','bbs','bca'], 'percentage':[70,59,65]}
# dfi=p.DataFrame(data1)
# print(dfi)
# data1={'Name':['simla','geeta','sita'],'Age':[22,23,24],'qualification':['bbs','bbs','bca'], 'percentage':[70,59,65]}
# dfi=p.DataFrame(data1, index=['rank1', 'rank2', 'rank3'])
# print(dfi)

# Create a DataFrame from List of Dicts
# data1=[{'x':1,'y':2},{'x':5,'y':6,'z':7}]
# df1=p.DataFrame(data1, index=['id1','id2'])
# print(df1)

# Create a DataFrame from Dict of Series
# d1={'one':p.Series([1,2,3],index=['a','b','c']),
#     'two':p.Series([1,2,3,4],index=['a','b','c','d'])}
# df1 = p.DataFrame(d1)
# # print(df1)
# df1['three']=p.Series([10,20,30],index=['a','b','c'])
# print(df1)
# df1['four']=df1['one']+df1['three']
# print(df1)

# Create a DataFrame from csv(comma separated value) file / import data
# from cvs file
# e.g.
# Suppose filename.csv file contains following data
# Date,"price","factor_1","factor_2"
# 2012-06-11,1600.20,1.255,1.548
# 2012-06-12,1610.02,1.258,1.554
# import pandas as pd
# # Read data from file 'filename.csv'
# # (in the same directory that your python program is based)
# # Control delimiters, rows, column names with read_csv
# data = pd.read_csv("filename.csv")
# # Preview the first 1 line of the loaded data
# data.head(1)


# Binary operation over dataframe with dataframe
# x=p.DataFrame({0:[1,2,3],1:[4,5,6],2:[7,8,9]})
# y=p.DataFrame({0:[2,3,4,],1:[4,5,6],2:[5,7,8]})
# new_x=x.add(y, axis=0)
# print(new_x)