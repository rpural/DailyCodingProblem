#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form 
racecar, which is a palindrome. daily should return false, since there's no 
rearrangement that can form a palindrome.
'''

import collections

def canPalindrome(string):
    breakdown = collections.Counter([c for c in string])
    pal = True
    odd = 0
    for c in breakdown:
        if breakdown[c] % 2 != 0:
            odd += 1
            if odd > 1:
                return False
    return True



if __name__ == '__main__':
    print(canPalindrome('carrace'))
    print(canPalindrome('daily'))
