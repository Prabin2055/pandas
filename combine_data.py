import pandas as pd


air_quality = pd.read_csv("air_quality.csv", parse_dates=True)
# air_quality_n2=air_quality[["datetime", "station_london"]]
# print(air_quality.head())


emp = pd.read_csv("testfile.csv", parse_dates=True)
emp2 = emp[["Name","Age", "Position", "salary"]]
# print(emp2)


### combine data from multiple tables

mul_data = pd.concat([air_quality, emp2],axis=0)
# print(mul_data.head())

air_quality2 = air_quality.sort_values("datetime") 
print(air_quality2)



### merge data

mer_mul = pd.merge(air_quality, emp, how="left", on="location")
print(mer_mul.head())
