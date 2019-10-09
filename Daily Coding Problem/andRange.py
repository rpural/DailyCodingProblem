#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Yahoo.

Write a function that returns the bitwise AND of all integers between M and N, inclusive.
'''

from functools import reduce

def andRange(m, n):
    return reduce( lambda x, y: x & y, range(m+1, n+1), m)

if __name__ == "__main__":
    print(f"andRange(5, 10) = {andRange(5, 10)}")
    print(f"andRange(2, 3)  = {andRange(2, 3)}")
