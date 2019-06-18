#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. 
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

       1
       2 3
       1 5 1
       We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, 
       eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is 
       the sum of the entries.

       Write a program that returns the weight of the maximum weight path.
'''

sample_path =  [[1], [2, 3], [1, 5, 1]] 

def maxpath(triangle, row=0, pos=0, sum=0, maxsum=0):
    depth = len(triangle)
    sum += triangle[row][pos]
    if row == depth-1:
        if sum > maxsum:
            return sum
        else:
            return maxsum
    if sum > maxsum:
        maxsum = sum
    left = maxpath(triangle, row+1, pos, sum, maxsum)
    right = maxpath(triangle, row+1, pos+1, sum, maxsum)
    return max(left, right, maxsum)

if __name__ == "__main__":
    print(maxpath(sample_path))
