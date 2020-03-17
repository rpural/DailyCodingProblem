#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
'''

def makeChange(amt, denominations):
    change = []

    for i in denominations:
        while i <= amt:
            change.append(i)
            amt -= i
    return change


if __name__ == "__main__":
    amt = 79
    denominations = [25, 10, 5, 1]

    change = makeChange(amt, denominations)
    print(f"{len(change)} coins: denominations: {change}")
