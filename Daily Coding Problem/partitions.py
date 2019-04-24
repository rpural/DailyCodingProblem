#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
'''

def partition(x, input):
    result = [l for l in input if l < x] + [e for e in input if e == x] + [g for g in input if g > x]
    return result


if __name__ == "__main__":
    sample = [ 9, 12, 3, 5, 14, 10, 10 ]

    print(sample)

    print( partition(10, sample))
