#! /usr/bin/env python3

import time
from latest_tutorial import fetch_tutorial
from timer import Timer

t = Timer()
t.start()
fetch_tutorial(0)
t.stop()
