import urllib
from pymongo import MongoClient
import pandas as pd
Connection_String="mongodb+srv://athiratv98:" +urllib.parse.quote("Rana@100408!") +"@cluster0.p0k5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client=MongoClient(Connection_String)
    print("Connected to mongo atlus is success")
    #Connect to mongo cluster (sample_mflix db name)
    db=client['ust_live_quiz']
    #access a collection
    collection=db['Basic_Collection_Test']

    #query the collection
    #query={'name':'Anusree'}

    query={'age':{"$gt":20}} #to find a set of values by applying condition
    results=collection.find(query) #if we want a subset of the data pass that variable inside find

    # for doc in results: #document is similar to row.collection like table,cluster is like db
    #     print(doc)
    #     break
except Exception as e:
    print(e)

print(type(results)) #result cursor object
result_list=list(results) #convert to list

df=pd.DataFrame(result_list)
print(df.head(100))
#print(df[['_id','name']].head())
#print(df.columns)
# print(type(result_list))#print type as list
# print(result_list[:4])


client.close()