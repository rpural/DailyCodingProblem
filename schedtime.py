#! /usr/bin/env python3

import sched
import time
from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

def saytime(): 
    print(time.ctime())
    scheduler.enter(10, priority=0, action=saytime)

saytime()
try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Stopped.')
