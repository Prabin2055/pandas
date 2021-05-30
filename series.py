"""
# pandas series

# import pandas as pseries
# s= pseries.Series()
# print(s)
 
# without index
import pandas as pd1
import numpy as np1
# data=np1.array(['a','b','c','d'])
# s=pd1.Series(data)
print(s)

# with index
data={'a':1, 'b':2,'c':3}
s=pd1.Series(data, index=['b', 'c', 'd'])
print(s)

"""

# # create a series from scalar

# import pandas as pd1
# import numpy as np1
# s=pd1.Series(5, index=[0,1,2,3])
# print(s)



# maths operations with series
# import pandas as p
# s=p.Series([1,2,3])
# t=p.Series([1,2,4])
# u=s+t
# v=s*t
# print(u)
# print(v)

# pandas head and tail 
# import pandas as p
# s=p.Series([1,2,3,4], index=['a','b','c','d'])
# print(s.head(3))
# print(s.tail(2))

# # retrieve data using label as index
# import pandas as p
# s=p.Series([1,2,3,4,5], index=['a','b','c','d','e'])
# print(s[['c','d']])


import pandas as pd
import numpy as np


s= pd.Series(np.random.randn(5), index=["a","b","c","d","e"])
print(s)
