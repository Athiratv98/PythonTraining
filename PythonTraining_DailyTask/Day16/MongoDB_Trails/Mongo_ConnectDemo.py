#lets connect mongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib

#uri="mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri="mongodb+srv://athiratv98:" +urllib.parse.quote("Rana@100408!") +"@cluster0.p0k5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# create a new client and connect to server
client=MongoClient(uri,server_api=ServerApi('1'),tlsAllowInvalidCertificates=True)

#sent a ping to confirm the successful connection
try:
    client.admin.command('ping')
    print("pinged your deployement.Successfully connected")
except Exception as e:
    print(e)