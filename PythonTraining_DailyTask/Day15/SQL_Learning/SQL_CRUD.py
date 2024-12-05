import sqlite3
connection=sqlite3.connect(r"C:\Users\Administrator\Desktop\PythonTraining\PythonTraining_DailyTask\Chinook_Sqlite.sqlite")
cursor=connection.cursor()
print(cursor)
#create operations
# new_customer=(60,'Rajiv','RR','UST','Rajiv@gmail.com','IND')
# cursor.execute(
#     """INSERT into Customer(CustomerId,Firstname,Lastname,Company,Email,Country) values(?,?,?,?,?,?)
#     """,new_customer
# )

# connection.commit()
# print("new cusyomer added")
#read the datas that are just wrote in to database
cursor.execute("select * from 'Customer' where CustomerID=60")
data=cursor.fetchall()
for row in data:
    print(row)
desc=cursor.description
cols=[col[0] for col in desc]
print(cols)

#updation
customer_id=60
customer_mail="rajivn456@ust.com"
cursor.execute(
    """
    update Customer 
    set Email=?,Company=?
    where CustomerId=?
    """,(customer_mail,"TCS",customer_id)
)
connection.commit()
print("Customer Updated")
cursor.execute("select * from 'Customer' where CustomerID=60")
data=cursor.fetchall()
for row in data:
    print(row)
desc=cursor.description
cols=[col[0] for col in desc]
print(cols)

# deletion
cursor.execute("Delete from Customer where CustomerID=60")

connection.commit()
print("ID 60 isdeleted")