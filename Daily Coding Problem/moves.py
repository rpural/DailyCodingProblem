#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you 
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum 
number of steps required to reach the end coordinate from the start. If there is 
no possible path, then return null. You can move up, left, down, and right. You 
cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

    [[f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]]
   
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number 
of steps required to reach the end is 7, since we would need to go through 
(1, 2) because there is a wall everywhere else on the second row.
'''

maze = [ [False, False, False, False],
         [True,  True,  False, True ],
         [False, False, False, False],
         [False, False, False, False] ]

start = (3, 0)
finish = (0, 0)

visited = []

for i in range(len(maze)):
    row = []
    for j in range(len(maze[0])):
        row.append(False)
    visited.append(row)

def test_path(startLoc, finLoc, step=0):
    (x, y) = startLoc
    (xd, yd) = finLoc
    minstep = 10000
    visited[x][y] = True
    step = step + 1

    cy = y
    for cx in range(x-1, x+2):
        if 0 <= cx < len(maze):
            if cx == xd and cy == yd:
                print("** ** Debug: cx={},cy={} - completed path in {} steps".format(cx, cy, step))
                return minstep
            if visited[cx][cy] or maze[cx][cy]:
                if maze[cx][cy]:
                    print("Debug: wall at cx={},cy={}, step {}".format(cx, cy, step))
                else:
                    print("Debug: already visited cx={},cy={}, step {}".format(cx, cy, step))
                continue
            print("Debug: testing cx={},cy={}, step {}".format(cx, cy, step))
            steps = test_path((cx,cy), (xd,yd), step)
            if steps < minstep:
                minstep = steps

    cx = x
    for cy in range(y-1, y+2):
        if 0 <= cy < len(maze[0]):
            if cx == xd and cy == yd:
                print("** ** Debug: cx={},cy={} - completed path in {} steps".format(cx, cy, step))
                return minstep
            if visited[cx][cy] or maze[cx][cy]:
                if maze[cx][cy]:
                    print("Debug: wall at cx={},cy={}, step {}".format(cx, cy, step))
                else:
                    print("Debug: already visited cx={},cy={}, step {}".format(cx, cy, step))
                continue
            print("Debug: testing cx={},cy={}, step {}".format(cx, cy, step))
            steps = test_path((cx,cy), (xd,yd), step)
            if steps < minstep:
                minstep = steps
    return minstep


steps = test_path(start, finish)
print("steps: {}".format(steps))
