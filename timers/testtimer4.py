#! /usr/bin/env python3

import time
from latest_tutorial import fetch_tutorial
from timer import timeit

@timeit
def fetch():
    return fetch_tutorial(0)


result = fetch()
