import urllib
from pymongo import MongoClient
import pandas as pd
#Connection_String=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
Connection_String="mongodb+srv://athiratv98:" +urllib.parse.quote("Rana@100408!") +"@cluster0.p0k5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client=MongoClient(Connection_String,tlsAllowInvalidCertificates=True)
    print("Connected to mongo atlus is success")
    #Connect to mongo cluster (sample_mflix db name)
    db=client['ust_live_quiz']
    #access a collection
    collection=db['Basic_Collection_Test']

    sample_data={
        'name':'Nirmay',
        'Age':3,
        'language':'Malayalam',
        'family':['Aruna','Ramya','Narayanan']
    }
    collection.insert_one(sample_data),
    print("insert successfully")
    #query the collection
    results=collection.find()
    # for doc in results: #document is similar to row.collection like table,cluster is like db
    #     print(doc)
    #     break
except Exception as e:
    print(e)

# print(type(results)) #result cursor object
result_list=list(results) #convert to list

df=pd.DataFrame(result_list)
print(df.head(100))
# print(df.columns)
# print(type(result_list))#print type as list
# print(result_list[:4])


client.close()