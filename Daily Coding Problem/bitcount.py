#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers 
between 1 and N.
'''

def bits_in_number(value):
    nbits = 0
    while value:
        nbits += value % 2
        value //= 2
    return nbits

while True:
    n = int(input("max value: "))
    if n == 0:
        break

    total = 0
    for i in range(1, n+1):
        total += bits_in_number(i)

    print(f"Total bits: {total:,}")
