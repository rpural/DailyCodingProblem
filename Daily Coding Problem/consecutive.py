#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Facebook.

Given a list of integers L, find the maximum length of a sequence of 
consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build 
a sequence [1, 2, 3, 4, 5] which has length 5.
'''

L = [5, 2, 99, 3, 4, 1, 100]

def consecutive(l):
    sl = sorted(L)
    count = 1
    maxcount = 1

    for i in range(1, len(sl)):
        if sl[i] == sl[i-1]+1:
            count += 1
            if i == len(sl) - 1:
                if count > maxcount:
                    maxcount = count
        else:
            if count > maxcount:
                maxcount = count
            count = 1

    return maxcount


if __name__ == "__main__":
    print(consecutive(L))
