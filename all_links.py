#! /usr/bin/env python3

''' Find all the links in a webpage '''

import requests
from bs4 import BeautifulSoup

res = requests.get("http://google.com")
html = res.text

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll('a')
for link in links:
    print(link)
