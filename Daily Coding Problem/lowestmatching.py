#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Amazon.

Given a sorted array arr of distinct integers, return the lowest index i for 
which arr[i] == i. Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even 
though arr[3] == 3, we return 2 since it's the lowest index.
'''

def lowestIndex(sequence):
    for i, val in enumerate(sequence):
        if val == i:
            return i
    return None

if __name__ == "__main__":
    print(lowestIndex((-5, -3, 2, 3)))
    print(lowestIndex([7,14,22,30]))
