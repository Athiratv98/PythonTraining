import pandas as pd
import numpy as np
data1={
    "name":['abc','xyz','frf'],
    "age":[34,24,23],
    "city":['fa','la','blr']
}
df=pd.DataFrame(data1)
data2={
    "name":['ath','ann','mng'],
    "age":[32,70,89],
    "city":['pnr','cochi','kan']
}
df1=pd.DataFrame(data2)
data3=pd.concat([df,df1],ignore_index=True)
df3=pd.DataFrame(data3)
df3.loc[2,'name']='athira'
print(df3)

print("-------")
df3.loc[df3['name']=='athira','city']='Chennai'
print(df3)

print("----------")
df3['city']=np.nan
print(df3)
print("-----")
df5=pd.concat([df,df1],ignore_index=True)