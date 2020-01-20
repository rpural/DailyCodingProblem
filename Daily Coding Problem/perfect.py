#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

import sys
from functools import reduce

def perfect(position):
    test = position
    digits = []
    while test > 0:
        digits.append(test % 10)
        test //= 10

    sum = reduce(lambda x,y: x + y, digits)
    if sum > 10:
        return None
    return position * 10 + (10 - sum)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("""run this program with one argument: the position of the
        perfect number to be found.""")
        exit(0)
    try:
        value = int(sys.argv[1])
    except:
        print("Could not convert argument to int")
        exit(1)

    if value < 1:
        print("argument must be a positive integer")
        exit(1)

    print(perfect(value))
