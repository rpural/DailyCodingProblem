#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in 
its binary representation.

For example, given 156, you should return 3.
'''

def onesRun(number):
    check = 1
    count = 0
    maxCount = 0

    while True:
        if number < check:
            return maxCount

        if number & check:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            count = 0

        check *= 2

if __name__ == "__main__":
    for i in (3, 5, 7, 15, 16, 156):
        print("Max run of 1 bits in {} is {}".format(i, onesRun(i)))

