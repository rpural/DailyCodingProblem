#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count 
the number of ways of starting at the top-left corner and getting to the 
bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two 
ways to get to the bottom-right:

    Right, then down
    Down, then right
    Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def walk_grid(x, y):
    maxx, maxy = x, y
    curx, cury = 1, 1

    successes = 0

    def step_grid(x, y):
        nonlocal successes
        if x == maxx - 1 and y == maxy - 1:
            successes += 1
            return
        if x < maxx -1:
            x += 1
            step_grid(x, y)
            x -= 1
        if y < maxy - 1:
            y += 1
            step_grid(x, y)
            y -= 1

    step_grid(0, 0)
    return successes


if __name__ == "__main__":
    print(f"2x2 grid: {walk_grid(2, 2)} paths")
    print(f"5x5 grid: {walk_grid(5, 5)} paths")
    print(f"10x10 grid: {walk_grid(10, 10)} paths")
    print(f"100x100 grid: {walk_grid(100, 100)} paths")
    print(f"100x2 grid: {walk_grid(100, 2)} paths")
