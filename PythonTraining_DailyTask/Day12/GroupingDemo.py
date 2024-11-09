import pandas as pd
data={
    'store':['store1','store1','store2','store2','store3','store3','store4','store5'],
    'region':['north','north','south','south','east','east','north','south'],
    'sales':[200,150,300,250,400,350,100,200]
}
df=pd.DataFrame(data)
print(df)

print(df.groupby(['store']).agg({'sales':"sum"}).reset_index())
print("----")
regional_sales_df=df.groupby(['region']).agg({'sales':"sum"}).reset_index()
print(regional_sales_df)

print("--------")
print(pd.merge(df,regional_sales_df,on='region',how='left',suffixes=('_store','_region')))