import requests
from bs4 import BeautifulSoup

# result= requests.get("https://www.google.com/")
# src=result.content
# soup=BeautifulSoup(src,'lxml')
# links=soup.find_all("a")
# for link in links:
#     if "About" in link.text:
#         print(link)
#         print(link.attrs['href'])
# print (links)
# print(result.status_code)

# results=requests.get("https://www.whitehouse.gov/briefings-statements/")
# src=results.content
# soup=BeautifulSoup(src,'lxml')
# urls=[]
# for h2_tag in soup.find_all("h2"):
#     a_tag=h2_tag.find("a")
#     try:
#         if 'href' in a_tag.attrs:
#            urls.append(a_tag.get('href'))
#     except:
#         pass

# print(urls)  

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""
with open('index.html','w') as f:
    f.write(html_doc)

soup=BeautifulSoup(html_doc,'lxml')

# print(soup.prettify())

# print(soup.find('b'))   # written first bold tag
# print(soup.find_all('b')) # written all

# get the
#  name of the tag
ag=soup.b
print(ag)
ag.name="blockquote"
print(ag)

ag=soup.find_all('b')[2]
print(ag.get('another-attribute'))
ag['another-attribute']=2
print(ag.get('another-attribute'))  # How to change the attributes
# Attributes 
# tag.attr['name']

