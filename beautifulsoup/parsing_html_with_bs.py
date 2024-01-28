import requests
from bs4 import BeautifulSoup

html = requests.get("http://localhost:8080/planets.html").text

soup = BeautifulSoup(html, "lxml")
#print(str(soup)[:1000])

#print(str(soup.html.body.div.table)[:200])

#print([str(c) for c in soup.html.body.div.table.children])

print(str(soup.html.body.div.table.tr.parent)[:200])