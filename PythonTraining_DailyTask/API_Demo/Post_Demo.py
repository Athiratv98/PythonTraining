import requests

url="https://jsonplaceholder.typicode.com/users"

data={
    "title":"Athira's Session",
    "body":"hello",
    "userId":1
}
response=requests.post(url,json=data)
print(response.json())