#! /usr/bin/env python3

''' Daily Coding problem

This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of 
1-bits on. For example, given the number 6 (0110 in binary), return 9 (1001).
'''

from collections import Counter

def cvt2bin(i):
    result = ""
    while i > 0:
        r = i % 2
        if r == 0:
            result = "0" + result
        else:
            result = "1" + result
        i = i // 2
    return result

def numBits(i):
    bin = cvt2bin(i)
    ct = Counter(bin)
    return ct["1"]


if __name__ == "__main__":
    while True:
        i = int(input("Enter an integer (-1 to end): "))
        if i == -1:
            break
        j = i + 1
        bits = numBits(i)
        while numBits(j) != bits:
            j = j +1

        print(f"Bit count for both {i} and {j} are {bits}.")


