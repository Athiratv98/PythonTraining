import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://unsplash.com/s/photos/nature"
response=requests.get(url)
# print(response.text)
# print(type(response.text))
soup=BeautifulSoup(response.text,'html.parser')
images=soup.find_all('img',{'srcset':True})
print(len(images))
image_url=images[-1]
image_url=image_url['src']
print(image_url)

image_data=requests.get(image_url).content
image_path="Sample_image.jpeg"
with open(image_path,'wb') as image_file_handler:
    image_file_handler.write(image_data)
for img in images:
    print("image source ",img.get('src'))