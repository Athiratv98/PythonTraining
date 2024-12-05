import sqlite3
import pandas as pd
connection=sqlite3.connect(r"C:\Users\Administrator\Desktop\PythonTraining\PythonTraining_DailyTask\Chinook_Sqlite.sqlite")
cursor=connection.cursor()
print(cursor)
# query="""
# select * from Customer limit 10
# """
# df_customer=pd.read_sql_query(query,connection)
# print(df_customer)
# connection.close()

#determine total sales for each country in the invoice table
# query="""
# select BillingCountry,sum(Total) as TotalSale
# from 'Invoice' group by BillingCountry

# """
# df_customer=pd.read_sql_query(query,connection)
# print(df_customer)
# connection.close()



#using pandas code"
query="""
select * from Invoice"""
df_customer=pd.read_sql_query(query,connection)
df_customer=df_customer.groupby('BillingCountry')['Total'].sum().reset_index()
print(df_customer)
# connection.close()

df_customer.to_sql('summary_sales_by_country',connection,if_exists='replace',index=False)
print("Data written into sqllite and printing the tables")
cursor.execute("select name from sqlite_master where type='table';")
tables=cursor.fetchall()
for table in tables:
    print(table)
connection.close()
