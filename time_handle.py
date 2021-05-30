import pandas as pd
import matplotlib.pyplot as plt


from pandas.core.groupby.generic import pin_whitelisted_properties

air = pd.read_csv("air_quality.csv")
# print(air)
# air = air.rename(columns={"datetime":"datetimes"})
# print(air)

air["datetime"] = pd.to_datetime(air["datetime"])
# print(air["datetime"])

print(air["datetime"].min())
print(air["datetime"].max())

# diff_time = air["datetime"].max()-air["datetime"].min()
# print(diff_time)

# air["month"]= air["month"].dt.month
# print(air.head())

# air.groupby([air["datetime"].dt.weekday, "location"])["value"].mean()



# fig, axis = plt.subplot(figsize=(12,4))
# air.groupby(air["datetime"].dt.hour)["value"].mean().plot(
#     kind= plt.bar, rot=0, ax=axis
# )
# plt.xlabel("houe of the day")
# plt.ylabel("$NO_2(g/m^3)$")


# no_2 = air.pivot(index="datetime", columns="location", values="value")
# no_2.head()
# no_2.index.year
# no_2.index.weekday



