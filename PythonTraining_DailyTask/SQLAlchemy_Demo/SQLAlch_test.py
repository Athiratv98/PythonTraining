from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Define the Database
DATABASE_URL="sqlite:///example.db"
Engine=create_engine(DATABASE_URL,echo=True)
Base=declarative_base()
SessionLocal=sessionmaker(bind=Engine)

#define a simple orm model
class User(Base):
    __tablename__="Users"
    Id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)

#create the Database and tables
Base.metadata.create_all(Engine)

#create a new session
session=SessionLocal()

# #create
# new_user=User(name="abc",age=26)
# session.add(new_user)
# session.commit()

#update
user_to_update=session.query(User).filter_by(Id=3).first()
if(user_to_update):
    user_to_update.name="Fathima"
    user_to_update.age=27
    print("update user")
    session.commit()

#delete
user_to_delete=session.query(User).filter_by(name='abc').first()
if(user_to_delete):
    session.delete(user_to_delete)
    print("User deleted")
    session.commit()

#Read
users=session.query(User).all()
print("All users")
for user in users:
    print(user.Id,user.name,user.age)

session.close()
