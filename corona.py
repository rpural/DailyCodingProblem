#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs

countrypop = dict()
page = requests.get("https://www.worldometers.info/world-population/population-by-country/")
soup = bs(page.text, 'html.parser')
tbl = soup.find("table", id="example2")
rows = tbl.find_all("tr")
del(rows[0]) # remove the headers
for row in rows:
    td = row.find_all("td")
    country = td[1].find("a").text
    population = td[2].text
    while population.find(",") > -1:
        population = population[:population.find(",")] + population[population.find(",")+1:]
    population = int(population)
    countrypop[country] = population


statepop = dict()
page = requests.get("https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population")
soup = bs(page.text, 'html.parser')
tbl = soup.find("table")
rows = tbl.find_all("tr")
del(rows[0]) # remove the headers
for row in rows:
    td = row.find_all("td")
    if td[0].text.isdecimal():
        state = td[2].find("a").text
        population = td[3].text
        while population.find(",") > -1:
            population = population[:population.find(",")] + population[population.find(",")+1:]
        population = int(population)
        statepop[state] = population

'''
page = requests.get("https://en.wikipedia.org/wiki/Template:2019-20_coronavirus_pandemic_data")
soup = bs(page.text, 'html.parser')
tbl = soup.find("table", id="thetable")
rows = tbl.find_all("tr")
for _ in range(2):
    del(rows[0])

for row in rows:
    th = row.find_all("th")
    if len(th) < 2:
        break
    anchor = th[1].find("a")
    country = anchor.string
    td = row.find_all("td")
    counts = []
    try:
        counts.append(td[0].string[:-1])
        counts.append(td[1].string[:-1])
        counts.append(td[2].string[:-1])
        for i in range(len(counts)):
            while counts[i].find(",") > -1:
                counts[i] = counts[i][:counts[i].find(",")] + counts[i][counts[i].find(",")+1:]
            try:
                counts[i] = int(counts[i])
            except ValueError:
                pass
    except TypeError:
        pass
    if country in countrypop:
        pop = countrypop[country]
    else:
        pop = '-'
    try:
        deathpct = counts[1] / pop
    except TypeError:
        deathpct = '-'

    pct = deathpct if deathpct == '-' else f'{deathpct*100:.4f}'
    if not isinstance(pop, int):
        pop = 0
    for i in range(len(counts)):
        if not isinstance(counts[i], int):
            counts[i] = 0
    try:
        print(f"{country:25s} {pop:15,d} cases:{counts[0]:14,d}, deaths:{counts[1]:14,d} =  {pct} deaths as pct of population")
    except TypeError:
        pass
'''

page = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States")
soup = bs(page.text, 'html.parser')
tbls = soup.find_all("table")
rows = tbls[5].find_all("tr")
for _ in range(0):
    del(rows[0]) # Remove headers
print(rows[0])

