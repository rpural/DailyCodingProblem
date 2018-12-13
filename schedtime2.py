#! /usr/bin/env python3

import sched
import time
from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

def reschedule():
     new_target = datetime.now().replace(
              second=0, microsecond=0)
     new_target += timedelta(minutes=1)
     scheduler.enterabs(
              new_target.timestamp(), priority=0, action=saytime)

def saytime():
     print(time.ctime(), flush=True)
     reschedule()
     
reschedule()

try:
     scheduler.run(blocking=True)
except KeyboardInterrupt:
     print('Stopped.')
