import pandas as pd
import matplotlib.pyplot as plt



# plt.plot([1,2,3,4])
# plt.ylabel('some numbr')
# plt.show()

air_quality = pd.read_csv("air_quality.csv", index_col=0, parse_dates=True)
# print(air_quality.head)
air_quality.plot()
plt.show()



# air_quality["station_paris"].plot()
# air_quality.show()


# air_quality.plot(["station_paris"])
# air_quality.xlabel("datetime")
# air_quality.show()