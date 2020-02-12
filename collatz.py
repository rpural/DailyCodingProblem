#! /usr/bin/env python3
'''
The collatz sequence is created by starting with any integer, and dividing 
even numbers by 2, or multiplying odd numbers by 3 and adding 1. The sequence
ends when you reach a value of 1.
'''

import sys

if len(sys.argv) < 2:
    print("Call with an integer value. This program will print the")
    print("Collatz Sequence equence of the given number.")
    exit(0)

try:
    value = int(sys.argv[1])
except ValueError as e:
    print("This program should be called with an integer value.")
    exit(1)

print(value)
while value != 1:
    if value % 2 == 0:
        value //= 2
    else:
        value = 3 * value + 1
    print(value)
