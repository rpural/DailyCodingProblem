#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
'''

import sys

denom = ( 25, 10, 5, 1 )  # Denominations of coins to use

result = []

amount = int(sys.argv[1])

for i in denom:
    while i <= amount:
        result.append(i)
        amount -= i

print("{} coins".format(len(result)))
print(result)
