#! /usr/bin/env python3

import time
from time import time as mytimer
import random

input("Press enter to start")
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = mytimer()

input("Press enter to stop")
end_time = mytimer()

print("started at", time.strftime("%X", start_time))
print("stopped at", time.strftime("%X", end_time))
print("reaction was {}".format(end_time - start_time))

