import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.theverge.com/"


r = requests.get(url)
htmlcontent = r.content
#print(htmlcontent)
soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify)
        
title = soup.title

#print(type(soup))
#print(type(title))
#print(type(title.string))

paras = soup.find_all('p')

anchors = soup.find_all('a')
for link in anchors:
    print(link.get('href'))
    

print(soup.find('p')['class'])

print(soup.find_all("p",class_ = "duet--article--dangerously-set-cms-markup"))

print(soup.find('p').get_text())

#print(soup.get_text())

anchors = soup.find_all('a')
all_link = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.theverge.com/" +link.get('href')
        all_link.add(link)
        print(linkText)
    
#for date in anchors:
    #print(date.get('span'))
