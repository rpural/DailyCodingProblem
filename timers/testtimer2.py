#! /usr/bin/env python3

import time
from latest_tutorial import fetch_tutorial
from timer import Timer

t = Timer("Download")

for i in range(0, 10):
    t.start()
    fetch_tutorial(i)
    t.stop()

print(f"Total download time: {t.timers['Download']:.4f} seconds.")
