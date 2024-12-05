import sqlite3
connection=sqlite3.connect(r"C:\Users\Administrator\Desktop\PythonTraining\PythonTraining_DailyTask\Chinook_Sqlite.sqlite")
cursor=connection.cursor()
print(cursor)
#cursor.execute("select name from sqlite_master where type='table';")
# tables=cursor.fetchall()
# for table in tables:
#     print(table)

cursor.execute("select * from 'Album' limit 10")
data=cursor.fetchall()
for row in data:
    print(row)
desc=cursor.description
cols=[col[0] for col in desc]
print(cols)