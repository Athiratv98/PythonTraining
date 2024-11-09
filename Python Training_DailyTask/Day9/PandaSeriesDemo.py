import pandas as pd
import numpy as np
arr=np.array([1,2,4,2,5])
#s=pd.Series(arr)
s=pd.Series(arr,index=['a','b','c','d','e'])
print(s)


s1=pd.Series(50,index=[1,2,3,4,5])
print(s1)

d={'name':'Athira','age':22,'place':'Kannur'}
s2=pd.Series(d)
print(s2)