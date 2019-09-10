#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Salesforce.

The number 6174 is known as Kaprekar's contant, after the mathematician who 
discovered an associated property: for all four-digit numbers with at least two 
distinct digits, repeatedly applying a simple procedure eventually results in 
this value. The procedure is as follows:

    For a given input x, create two new numbers that consist of the digits in x 
    in ascending and descending order.
    Subtract the smaller number from the larger number.

    For example, this algorithm terminates in three steps when starting from 1234:

    4321 - 1234 = 3087
    8730 - 0378 = 8352
    8532 - 2358 = 6174
    Write a function that returns how many steps this will take for a given input N.
'''

kaprekar = 6174

def resolve(value, iterations=0):
    svalue = f"{value}"
    while len(svalue) < 4:
        svalue = "0" + svalue
    lvalue = list(svalue)
    lvalue.sort()
    svalue = "".join(lvalue)
    v1 = int(svalue)
    v2 = int(''.join(reversed(svalue)))
    newValue = max(v1, v2) - min(v1, v2)
    iterations += 1

    if newValue == kaprekar:
        return iterations
    else:
        return resolve(newValue, iterations)


for v in (1234, 1235, 6436):
    vi = resolve(v)
    print("The value {} resolves to {} in {} iterations.".format(v, kaprekar, vi))


for v in (x for x in range(4010,4245)):
    vi = resolve(v)
    print("The value {} resolves to {} in {} iterations.".format(v, kaprekar, vi))
