#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. 
Given a sorted array of distinct elements, return a fixed point, if one exists. 
Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], 
you should return False.
'''

test1 = [ -6, 0, 2, 40 ]
test2 = [ 1, 5, 7, 8 ]

def hasFixedPoint(l):
    ls = l.copy()
    ls.sort()
    for i in range(len(ls)):
        if ls[i] == i:
            return i
    return False


if __name__ == "__main__":
    print(f"Method 1: List {test1} yields {hasFixedPoint(test1)}")
    print(f"Method 1: List {test2} yields {hasFixedPoint(test2)}")
