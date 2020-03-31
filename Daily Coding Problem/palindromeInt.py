#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, 
121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert 
the integer into a string.
'''

def reverseNum(num):
    result = 0
    while num > 0:
        digit = num % 10
        result *= 10
        result += digit
        num //= 10
    return result

def isPalindrome(num):
    rnum = reverseNum(num)
    if rnum == num:
        return True
    return False

if __name__ == "__main__":
    tests = [5, 12, 22, 121, 1234321, 1324563]
    for i in tests:
        print(f"{i:9d} - {isPalindrome(i)}")

