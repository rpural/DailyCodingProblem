#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list so that 
all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the 
solution could be 1 -> 0 -> 5 -> 8 -> 3.
'''

def pivot(lst, breakpoint):
    lb = []
    la = []

    for i in lst:
        if i < breakpoint:
            lb.append(i)
        else:
            la.append(i)

    return lb + la


if __name__ == "__main__":
    samples = [[[5,1,8,0,3], 3],
               [[1,10,25,20,18,3,7,15,13,10,1,20,17,5,7,9], 14]
              ]

    for l, p in samples:
        print(f"before: {l}, pivot: {p}")
        print(f" after: {pivot(l, p)}\n")
