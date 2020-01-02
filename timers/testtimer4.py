#! /usr/bin/env python3

import time
from latest_tutorial import fetch_tutorial
from timer import Timer

@Timer()
def fetch(text="Downloaded the tutorial in {:.2f} seconds"):
    return fetch_tutorial(0)


result = fetch()
