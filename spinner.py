#! /usr/bin/env python3

'''
    Create a spinner to mark time...
'''

from itertools import cycle
from time import sleep

for frame in cycle(r'-\|/-\|/'):
        print('\r', frame, sep='', end='', flush=True)
        sleep(0.2)
