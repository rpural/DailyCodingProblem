#! /usr/bin/env python3

''' Daily Coding problem

This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
'''

number = int(input("Enter a number: "))

string = str(number)
print(f"The number of digits in the number is: {len(string)}")
