#! /usr/bin/env python3

'''
    Print the number of days until retirement
'''

import datetime

today_ = datetime.date.today()
retire = datetime.date(2020,5,31)
delta = retire - today_

print(f"{delta.days} days until retirement...")
