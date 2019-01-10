#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

import random

def rand5():
    return random.randrange(1, 6)

def rand7():
    return int( (rand5() / 5) * 7 )

for i in range( 100 ):
    print(rand5())

print("*" * 5)

for i in range( 100 ):
    print(rand7())
