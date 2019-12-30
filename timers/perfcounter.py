#! /usr/bin/env python3

import time
from latest_tutorial import fetch_tutorial 

tic = time.perf_counter()
fetch_tutorial(0)
toc = time.perf_counter()

print(f"Downloaded and printed the tutorial in {toc - tic:-.4f} seconds")
