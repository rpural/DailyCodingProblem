#! /usr/bin/env python3

'''
Write a program that prints all pairs of two digit numbers whose product matches
the product of the two numbers with their digits reversed.
'''

from timer import Timer

with Timer() as t:
    pairs = set()
    for i in range(10, 100):
        for j in range(i, 100):
            ri = int("".join((reversed(str(i)))))
            rj = int("".join((reversed(str(j)))))
            if i * j == ri * rj:
                pairs.add((ri, rj))

print("Request took {:.03f} sec.".format(t.interval))

print(f"\npairs: {pairs}")
print(f"count: {len(pairs)}\n\n")

with Timer() as t:
    pairs = [(x,y) for x in range(10, 100) for y in range(x, 100) if x * y == int("".join(reversed(str(x)))) * int("".join(reversed(str(y))))]

print("Request took {:.03f} sec.".format(t.interval))

print(f"\npairs: {pairs}")
print(f"count: {len(pairs)}")
