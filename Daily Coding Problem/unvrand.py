#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with 
uniform probability, implement a function rand7() that returns an integer from 
1 to 7 (inclusive).
'''

import random
import statistics

def rand5():
    return random.randint(1, 5)


def rand7():
    total = 1
    for i in range(200):
        total += rand5()
    return total % 7 + 1


from collections import Counter

distrib = Counter()

# first, to check the distribution of our source, generate 10000 random numbers
distrib.update([rand5() for x in range(10000)])

print(f"Distribution for rand5:  ", end="")
for i in range(1,6):
    print(f"{i}: {distrib[i]}", end=", ")

print(f"\n  standard deviation: {statistics.pstdev(distrib.values()):0.3f}")


distrib = Counter()

# now test rand7() to see if it is also evenly distributed
distrib.update([rand7() for x in range(10000)])

print(f"Distribution for rand7:  ", end="")
for i in range(1,8):
    print(f"{i}: {distrib[i]}", end=", ")

print(f"\n  standard deviation: {statistics.pstdev(distrib.values()):0.3f}")
