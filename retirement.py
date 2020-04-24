#! /usr/bin/env python3

'''
    Print the number of days until retirement
'''

import datetime

today_ = datetime.date.today()
retire = datetime.date(2020,5,31)
furlough = datetime.date(2020,5,21)
delta = retire - today_
delta_short = furlough - today_

print(f"{delta.days} days until retirement...")
print(f"{delta_short.days} days until furlough...")
