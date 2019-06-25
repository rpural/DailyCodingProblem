#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1
    It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

    Bonus: What input n <= 1000000 gives the longest sequence?

'''

longest = (0, 0)
results = dict()

for i in range(2, 1_000_001):
    n = i
    steps = 0
    while n != 1:
        if n in results:
            steps += results[n]
            break
        else:
            if n % 2 == 1:
                n = 3 * n + 1
            else:
                n = n / 2
            steps += 1
    if steps > longest[1]:
        longest = (i, steps)
    results[i] = steps

print("Longest number of steps: ({}, {})".format(longest[0], longest[1]))
