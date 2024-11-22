import urllib
from pymongo import MongoClient
import pandas as pd
Connection_String="mongodb+srv://athiratv98:" +urllib.parse.quote("Rana@100408!") +"@cluster0.p0k5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client=MongoClient(Connection_String)
    print("Connected to mongo atlus is success")
    #Connect to mongo cluster (sample_mflix db name)
    db=client['sample_mflix']
    #access a collection
    collection=db['movies']
    #query the collection
    results=collection.find().limit(5)
    # for doc in results: #document is similar to row.collection like table,cluster is like db
    #     print(doc)
    #     break
except Exception as e:
    print(e)

print(type(results)) #result cursor object
result_list=list(results) #convert to list

df=pd.DataFrame(result_list)

print(df.head())
print(df.columns)
# print(type(result_list))#print type as list
# print(result_list[:4])


client.close()