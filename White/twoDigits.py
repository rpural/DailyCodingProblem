#! /usr/bin/env python3

'''
Write a program that prints all pairs of two digit numbers whose product matches
the product of the two numbers with their digits reversed.
'''

pairs = set()
for i in range(10, 100):
    for j in range(i, 100):
        ri = int("".join((reversed(str(i)))))
        rj = int("".join((reversed(str(j)))))
        if i * j == ri * rj:
            pairs.add((ri, rj))

print(f"pairs: {pairs}")
print(f"count: {len(pairs)}")

pairs = [(x,y) for x in range(10, 100) for y in range(x, 100) if x * y == int("".join(reversed(str(x)))) * int("".join(reversed(str(y))))]
print(f"\npairs: {pairs}")
print(f"count: {len(pairs)}")
