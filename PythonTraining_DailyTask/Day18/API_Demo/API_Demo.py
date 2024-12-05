import requests
import pandas as pd
url="https://jsonplaceholder.typicode.com/users"

#lets try the get()
response=requests.get(url)
if(response.status_code==200):
    print("Everything went well")

    print(response.json())
else:
    print("Something went wrong",str(response.status_code))

df=pd.DataFrame(response.json())
print(df)
