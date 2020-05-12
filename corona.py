#! /usr/bin/env python3

'''
    Coronavirus (CoVID-19) statistics

    With all the numbers being thrown around, the one statistic I was
    curious about, but never saw in any of the reporting, was the number
    of deaths due to coronavirus compared to the country's (or geographic
    area's) population.

    So, this program collects a list of country and U.S. state populations,
    and then the CoVID-19 statistics for countries and for states. The 
    report produced first lists the countries, with populations, cases, 
    deaths, and the percentage of deaths against the population. Then it
    will produce the same report for the U.S. states.
'''

import requests
from bs4 import BeautifulSoup as bs

def remove_commas(value):
    ''' Utility function:
        Given a string, find and remove the commas from a formatted number,
        remove any trailing fluff,
        and convert it to an integer. '''
    while value.find(",") > -1:
        value = value[:value.find(",")] + value[value.find(",")+1:]
    if not value.isnumeric():
        for i in range(len(value)):
            if not value[i].isnumeric():
                value = value[:i]
                break
    try:
        value = int(value)
    except ValueError:
        print(f"[debug] value contains {value}")
        pass
    return value


def country_populations():
    ''' Collect a dictionary of country populations, keyed by country name,
        and return it to the caller '''
    countrypop = dict()
    page = requests.get("https://www.worldometers.info/world-population/population-by-country/")
    soup = bs(page.text, 'html.parser')
    tbl = soup.find("table", id="example2")
    rows = tbl.find_all("tr")
    for row in rows[1:]:
        td = row.find_all("td")
        country = td[1].find("a").text
        population = td[2].text
        population = remove_commas(population)
        countrypop[country] = population
    return countrypop


def state_populations():
    ''' Collect a dictionary of U.S. state populations, keyed by state name,
        and return it to the caller '''
    statepop = dict()
    page = requests.get("https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population")
    soup = bs(page.text, 'html.parser')
    tbl = soup.find("table")
    rows = tbl.find_all("tr")
    for row in rows[1:]:
        td = row.find_all("td")
        if td[2].find("a") != None:
            state = td[2].find("a").text
            population = td[3].text
            population = remove_commas(population)
            statepop[state] = population
    return statepop


def country_statistics():
    ''' Get and report on Coronavirus statistics by country '''
    page = requests.get("https://en.wikipedia.org/wiki/Template:2019-20_coronavirus_pandemic_data")
    soup = bs(page.text, 'html.parser')
    tbl = soup.find("table", id="thetable")
    rows = tbl.find_all("tr")
    for _ in range(2):
        del(rows[0])

    print(f"{'country':25s} {'population':>15s} {'cases':>14s} {'deaths':>14s}    {'cases/M'}    {'deaths/M'}")
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
            popscale = pop / 1_000_000
            case_per_m = counts[0] / popscale
            death_per_m = counts[1] / popscale
        except TypeError:
            case_per_m = '-'
            death_per_m = '-'

        case_per_m = "     -   " if case_per_m == '-' else f'{case_per_m:9.3f}'
        death_per_m = "     -   " if death_per_m == '-' else f'{death_per_m:9.3f}'
        if not isinstance(pop, int):
            pop = 0 
        for i in range(len(counts)):
            if not isinstance(counts[i], int):
                counts[i] = 0
        try:
            print(f"{country:25s} {pop:15,d} {counts[0]:14,d} {counts[1]:14,d}   {case_per_m}   {death_per_m}")
        except TypeError:
            pass


def state_statistics():
    ''' Get U.S. state CoVID-19 statistics and produce a report '''
    page = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States")
    soup = bs(page.text, 'html.parser')
    print(f"{'State':25s} {'population':>15s} {'cases':>14s} {'deaths':>14s}    {'cases/M'}    {'deaths/M':6s}")
    tbls = soup.find_all("table")
    # The table has moved around some, so look at the first field of each table and find
    # the one containing 'COVID-19_pandemic_data/United_States_medical_cases_by_state'
    for tbl in tbls:
        row = tbl.find("tr")
        if "COVID-19 pandemic in the United States by state and territory" in row.text:
            rows = tbl.find_all("tr")
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
                    popscale = pop / 1_000_000
                    case_per_m = counts[0] / popscale
                    death_per_m = counts[1] / popscale
                except TypeError:
                    case_per_m = '-'
                    death_per_m = '-'
                except ValueError:
                    case_per_m = '-'
                    death_per_m = '-'
                except ZeroDivisionError:
                    case_per_m = '-'
                    death_per_m = '-'

                case_per_m = "     -   " if case_per_m == '-' else f'{case_per_m:9.3f}'
                death_per_m = "     -   " if death_per_m == '-' else f'{death_per_m:9.3f}'
                pop = pop if pop == '-' else f'{pop:15,d}'
                try:
                    print(f"{state:25s} {pop:15s} {counts[0]:14,d} {counts[1]:14,d}   {case_per_m}   {death_per_m}")
                except TypeError:
                    pass
                except ValueError:
                    print(f"{state:25s} {pop} cases: {counts[0]}, {counts[1]}")


if __name__ == "__main__":
    import datetime

    countrypop = country_populations()
    statepop = state_populations()

    print(f"CoVID-19 Statistics as of {datetime.date.today().strftime('%m/%d/%Y')}\n")

    print("CoVID-19 Statistics by Country")
    print()
    country_statistics()

    print()
    print("=" * 40)
    print()

    print("CoVID-19 Statistics by State in the United States")
    print()
    state_statistics()
