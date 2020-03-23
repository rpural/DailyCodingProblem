#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''

from itertools import permutations

a = [[1, 2, 3],
     [1, 2, 3, 4, 5],
     [1,2],
     [1]]

for input_ in a:
    result = list(permutations(input_, len(input_)))
    print(f"for {input_}, result is {result}")
    print(f"{len(result)} permutations")
