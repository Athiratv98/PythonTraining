import pandas as pd
name=pd.Series(['Hardik','Virat'],index=['Rank1','Rank2'])
team=pd.Series(['MI','RCB'],index=['Rank1','Rank2'])
dic={'Name':name,'Team':team}
df=pd.DataFrame(dic)
print(df)

print("-------------")
for row_index,row_value in df.iterrows():
    print('Row index is ',row_index)
    print('Row value is ',row_value)