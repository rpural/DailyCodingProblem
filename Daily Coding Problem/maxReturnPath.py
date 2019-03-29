#! /usr/bin/env python3

''' Daily Coding Problem

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
'''

def search(board, locx=0, locy=0, total=0):
    total += board[locx][locy]
    value = total
    if locy == len(board[locx]) -1 and locx == len(board) - 1:
        return total

    if locy < len(board[locx]) - 1:
        trial = search(board, locx, locy + 1, value)
        if trial > total:
            value = trial

    if locx < len(board) - 1:
        trial = search(board, locx + 1, locy, total)
        if trial > total:
            value = trial

    return value


board = [[0, 3, 1, 1],
         [2, 0, 0, 4],
         [1, 5, 3, 1]]

print("Matrix:")
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end=" ")
    print()
print()

print("maximum weighted path returns {}".format(search(board)))