import pandas as pd
import numpy as np
data1={
    "name":['RRR','ABC','XYZ',"Athira"],
    "age":[34,24,23,26],
    "city":['Banglore','Chennai','Hyderbad','Payyanur']
}
df1=pd.DataFrame(data1)
print("----------")
print(df1)
data2={
    "name":['RRR','ABC','XYZ'],
    "Work experience":[1,2,3],
    "city":['NYC','BRK','LA']
}
df2=pd.DataFrame(data2)
print("----------")
print(df2)
print("----------")
df3=pd.merge(df1,df2,on='name',how='outer')
print(df3)
df3.loc[df3['name']=='Athira','Work experience']=df3['Work experience'].mean()
print(df3)
df3.to_csv("csvdemo.csv",index=False)
# how