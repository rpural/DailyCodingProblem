#! /usr/bin/env python3

''' Daily Coding Problem
This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the 
points. Give the minimum number of steps in which you can achieve it. You start 
from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move 
from (1, 1) to (1, 2).
'''

from math import floor, sqrt

def traverse(points):
    location = points[0]
    dist = 0
    for p in points[1:]:
        dist += floor(sqrt(abs(location[0] - p[0]) ** 2 + abs(location[1] - p[1]) ** 2))
        location = p
    return dist


map = [(0,0), (1,1), (1,2)]
print(traverse(map))

map = [(5,4), (7,3), (0,5)]
print(traverse(map))


