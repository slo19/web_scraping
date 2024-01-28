import requests
from bs4 import BeautifulSoup

html = requests.get("http://localhost:8080/planets.html").text

soup = BeautifulSoup(html, "lxml")
print(str(soup)[:1000])