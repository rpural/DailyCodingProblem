#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs

def remove_commas(value):
    while value.find(",") > -1:
        value = value[:value.find(",")] + value[value.find(",")+1:]
    try:
        value = int(value)
    except ValueError:
        pass
    return value


# Get country populations for use later
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
    population = remove_commas(population)
    countrypop[country] = population


# Get state populations for use later
statepop = dict()
page = requests.get("https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population")
soup = bs(page.text, 'html.parser')
tbl = soup.find("table")
rows = tbl.find_all("tr")
del(rows[0]) # remove the headers
for row in rows:
    td = row.find_all("td")
    if td[2].find("a") != None:
        state = td[2].find("a").text
        population = td[3].text
        population = remove_commas(population)
        statepop[state] = population

# Get coronavirus statistics by country
page = requests.get("https://en.wikipedia.org/wiki/Template:2019-20_coronavirus_pandemic_data")
soup = bs(page.text, 'html.parser')
tbl = soup.find("table", id="thetable")
rows = tbl.find_all("tr")
for _ in range(2):
    del(rows[0])

print(f"{'country':25s} {'population':>15s} {'cases':>14s} {'deaths':>14s}   {'% deaths/pop'}")
for row in rows:
    th = row.find_all("th")
    if len(th) < 2:
        break
    anchor = th[1].find("a")
    country = anchor.string
    td = row.find_all("td")
    counts = []
    counts.append(td[0].string[:-1])
    counts.append(td[1].string[:-1])
    for i in range(len(counts)):
        counts[i] = remove_commas(counts[i])
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
        print(f"{country:25s} {pop:15,d} {counts[0]:14,d} {counts[1]:14,d}   {pct}")
    except TypeError:
        pass

print()
print("=" * 40)
print()

page = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States")
soup = bs(page.text, 'html.parser')
print(f"{'State':25s} {'population':>15s} {'cases':>14s} {'deaths':>14s}   {'% deaths/pop':6s}")
tbls = soup.find_all("table")
rows = tbls[5].find_all("tr")
for _ in range(3):
    del(rows[0]) # Remove headers
for row in rows:
    th = row.find_all("th")
    if len(th) < 2:
        break
    anchor = th[1].find("a")
    state = anchor.string
    td = row.find_all("td")
    counts = []
    for i in range(2):
        counts.append(td[i].text)
    for i in range(len(counts)):
        counts[i] = remove_commas(counts[i])
    if state in statepop:
        pop = statepop[state]
    else:
        pop = 0
    try:
        deathpct = counts[1] / pop
    except TypeError:
        deathpct = '-'
    except ValueError:
        deathpct = '-'
    except ZeroDivisionError:
        deathpct = '-'

    pct = deathpct if deathpct == '-' else f'{deathpct*100:.4f}'
    pop = pop if pop == '-' else f'{pop:15,d}'
    try:
        print(f"{state:25s} {pop:15s} {counts[0]:14,d} {counts[1]:14,d}   {pct}")
    except TypeError:
        pass
    except ValueError:
        print(f"{state:25s} {pop} cases: {counts[0]}, {counts[1]} - {pct}")

