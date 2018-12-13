#! /usr/bin/env python3

''' Daily Coding Problem #5

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

    def cons(a, b):
        def pair(f):
                return f(a, b)
        return pair

Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(consCall):
    def returnFirst(a, b):
        return a
    return consCall(returnFirst)

def cdr(consCall):
    def returnLast(a, b):
        return b
    return consCall(returnLast)

cons(1, 2)(print)

print( car(cons(1,2)) )

print( cdr(cons(1,2)) )
