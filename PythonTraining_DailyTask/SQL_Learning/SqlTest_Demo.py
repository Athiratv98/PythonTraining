import sqlite3
connection=sqlite3.connect(r"C:\Users\Administrator\Desktop\PythonTraining\PythonTraining_DailyTask\SQL_Learning\Chinook_Sqlite.sqlite")
cursor=connection.cursor()
print(cursor)