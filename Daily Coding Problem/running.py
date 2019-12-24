#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Airbnb.

Given an array of integers, return the largest range, inclusive, of integers 
that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) 
since 8, 9, 10, 11, and 12 are all in the array.
'''

def find_running(seq):
    lcl = sorted(seq)

    result = None
    longest = 0
    loc = 0
    c = 1
    print(f"[debug] longest = {longest}, loc = {loc}, c = {c}")

    for p, i in enumerate(lcl):
        print(f"[debug] new iteration: position = {p}, value = {i}")
        if p < len(lcl) - 1 and i == lcl[p+1] - 1:

            c += 1
            if c > longest:
                longest = c
                loc = p+2 - c
            else:
                c = 1
            print(f"[debug] Extending sequence: c = {c}, longest = {longest}, location = {loc}, seq = {lcl[loc:p+1]}")
    return (lcl[loc], lcl[loc+longest-1])


if __name__ == "__main__":
    test =  [9, 6, 1, 3, 8, 10, 12, 11] 
    result = find_running(test)

    print(f"bounded running sequence within {test} is {result}")
