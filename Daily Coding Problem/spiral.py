#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

    [[1,  2,  3,  4,  5],
     [6,  7,  8,  9,  10],
      [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]
       You should print out the following:

       1
       2
       3
       4
       5
       10
       15
       20
       19
       18
       17
       16
       11
       6
       7
       8
       9
       14
       13
       12
       '''

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

width = len(matrix[0])
height = len(matrix)

print("width = {}, height = {}".format(width, height))
for i in matrix:
    print(i)

ws = 0
hs = 0
w = width
h = height

while (ws < w) and (hs < h):
    for i in range(ws, w):
        print(matrix[hs][i])
    hs += 1
    for i in range(hs, h):
        print(matrix[i][w-1])
    w -= 1
    for i in range(w-1, ws-1, -1):
        print(matrix[h-1][i])
    h -= 1
    for i in range(h-1, hs, -1):
        print(matrix[i][ws])
    ws += 1
