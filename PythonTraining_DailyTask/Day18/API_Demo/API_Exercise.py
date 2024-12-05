import requests

url="https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand"

response=requests.get(url)
if(response.status_code==200):
    print("Everything went well")
else:
    print("Something went wrong",str(response.status_code))

#post

data={
    "title":"Athira's Session",
    "content":"hello",
    "id":1
}
post_data=requests.post(url,json=data)
print(post_data.json())