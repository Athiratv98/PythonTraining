import urllib
from pymongo import MongoClient
import pandas as pd
from bson.objectid import ObjectId
#Connection_String=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
Connection_String="mongodb+srv://athiratv98:" +urllib.parse.quote("Rana@100408!") +"@cluster0.p0k5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client=MongoClient(Connection_String,tlsAllowInvalidCertificates=True)
    print("Connected to mongo atlus is success")
    #Connect to mongo cluster (sample_mflix db name)
    db=client['ust_live_quiz']
    #access a collection
    collection=db['Basic_Collection_Test']

   
    #update the collection
    doc_id="67405788a82fc70b39b088c0"
    query={"_id":ObjectId(doc_id)}
    update={"$set":{"Films":"English movies","places":"TVM"} }
    updated_data=collection.update_one(query,update)
    if(updated_data.matched_count>0):
        print("THere is a mathc!document has been found")
    
    #print(df['_id','Name'])
    #print("updated successfully")
        
except Exception as e:
    print(e)





client.close()