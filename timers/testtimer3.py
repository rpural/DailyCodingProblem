#! /usr/bin/env python3

import time
from latest_tutorial import fetch_tutorial
from timer import Timer

with Timer():
    fetch_tutorial(0)
