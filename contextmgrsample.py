#! /usr/bin/env python

from time import perf_counter
from contextlib import contextmanager

from array import array

@contextmanager
def timing(label):
    t0 = perf_counter()
    yield lamda: (label, t1 - t0)
    t1 = perf_counter()

with timing('Array tests' as total:
    with timing('Array creation - inner mul') as inner:
        x = array('d', [0] * 1000000)

    with timing('Array creation - outer mul') as outer:
        x = array('d', [0]) * 1000000

print('Total [%s]: %.6f s' % total())
print('\tTiming [%s]: %.6f s' % inner())
print('\tTiming [%s]: %.6f s' % outer())
