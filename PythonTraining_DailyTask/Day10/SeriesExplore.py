#implement any 5 method in a series and any 5 attribute in series

import pandas as pd
data=pd.Series(['abc',20,'xyz'],index=['name','age','place'])
data1=data.tolist() # series to list1
print(data1)

#to drop an item from series
data2=data.drop('name')
print(data2)