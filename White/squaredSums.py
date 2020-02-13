#! /usr/bin/env python3
'''
The number 3025 has the following characteristic: 30 + 25 = 55 and 55**2 = 3025.
Write a program that prints all numbers with four digits that have the aforementioned
characteristic.
'''

for i in range(1000, 10_000):
    istr = str(i)
    sqsum = (int(istr[:2]) + int(istr[2:])) ** 2
    if sqsum == i:
        print(i)


print([x for x in range(1000, 10_000) if ((int(str(x)[:2]) + int(str(x)[2:])) ** 2) == x])
