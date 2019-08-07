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

jumps = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]

def minjumps(maxjump, position=0, jumps=0, minj=None):
    if minj == None:
        print("initially setting minj from {}".format(maxjump))
        minj = len(maxjump)
    if position == len(maxjump) - 1:
        print("found end of list in {} jumps".format(jumps))
        if jumps < minj:
            minj = jumps
        return minj
    if maxjump[position] == 0:
        print("stalled at position {}, aborting".format(position))
        return minj
    for i in range(maxjump[position], 0, -1):
        print("jump {}, position {} with step {}".format(jumps, position, i))
        newpos = position + i
        if newpos >= len(maxjump):
            print("past end of array, nonviable solution. aborting")
            continue
        newminj = minjumps(maxjump, position=newpos, jumps=jumps+1, minj=minj)
        print("newminj = {}, minj = {}, position = {}, step = {},jumps = {}".format(newminj, minj, position, jumps, i))
        if newminj == None:
            print("minjumps() returned None")
        elif newminj < minj:
            minj = newminj


if __name__ == "__main__":
    print(minjumps(jumps))
