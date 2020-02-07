#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of 1-bits 
on. For example, given the number 6 (0110 in binary), return 9 (1001).
'''

from collections import Counter

def find_next(value):
    binString = f'{value:b}'
    c = Counter(binString)
    ones = c['1']

    nx = value + 1
    while Counter(f'{nx:b}')["1"] != ones:
        nx += 1

    return nx


if __name__ == "__main__":
    for i in (6, 15, 113, 115, 12_345, 1_234_567_890):
        x = find_next(i)
        print(f"test value: {i} ({i:b}) -> {x} ({x:b}), count = {Counter(f'{x:b}')['1']}")
