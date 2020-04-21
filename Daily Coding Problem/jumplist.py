#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Yelp.

You are given an array of integers, where each element represents the maximum 
number of steps that can be jumped going forward from that element. Write a 
function to return the minimum number of jumps you must take in order to get 
from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the 
optimal solution involves jumping from 6 to 5, and then from 5 to 9.
'''

def jumplist(l):
    current = 0
    jumps = 0

    while current < ( len(l) - 1 ):
        maxjump = 0
        maxloc = 0
        m = l[current]
        
        if current + m < len(l):
            for i in range(current+1, current+m+1):
                if i < len(l):
                    if l[i]+current >= maxjump+current:
                        maxjump = l[i]
                        maxloc = i

        else:
            current += m

        jumps += 1
        current = maxloc if maxloc > 0 else len(l) - 1

    return jumps

if __name__ == "__main__":
    samples = [[6, 2, 4, 0, 5, 1, 1, 4, 2, 9],
               [1, 1, 1, 1, 1],
               [6, 1, 1, 1],
               [3, 2, 9, 5, 6, 7, 3, 4, 5, 7, 5, 3, 2, 4, 3, 2, 5],
               [9, 8, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]]

    for s in samples:
        print(f"{jumplist(s)} jumps for {s}")
    print("\nCorrect answers should be 2, 4, 1, 3,  3")
