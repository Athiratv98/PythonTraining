import requests
from bs4 import BeautifulSoup
url="https://example.com"
response=requests.get(url)
print(response.text)
print(type(response.text))
soup=BeautifulSoup(response.text,'html.parser')
#print(soup)
print("Heading---------")
h1_tag=soup.find('h1')
if(h1_tag):
    print(h1_tag.text)
print("links-----------------")
link=soup.find_all('a')
for links in link:
    href=links.get('href')
    print(href)
print("Paraghraphs------------------")
paragragh=soup.find_all('p')
for p in paragragh:
    print(p.text)