#! /usr/bin/env python

import requests

basePage = "https://xkcd.com"
URI = "info.0.json"

r = requests.get( basePage + '/' + URI )

if r.status_code == 200:
    entry = r.json()
    max = int( entry["num"] )

    for i in range( max, 0, -1 ):
        r = requests.get( basePage + '/' + str(i) + '/' + URI )
        if r.status_code == 200:
            entry = r.json()
            print( str( entry["num"] ) + "\t" + str( entry["year"] ) + "/" + str( entry["month"] ) + "/" + str( entry["day"] ) + "\t" +entry["title"] )
