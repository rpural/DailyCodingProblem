#! /usr/bin/env python3

''' 
    Test collecting metadata about a function by adding attributes dynamically
'''

def f(value):
    ''' Recursively calculate a factorial '''

    if hasattr(f, 'callcount'):
        f.callcount += 1
    else:
        f.callcount = 1

    if value <= 1:
        return 1
    return value * f(value-1)

print(f(5))

print(f"call count for f is {f.callcount}")
