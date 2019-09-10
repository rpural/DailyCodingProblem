#! /usr/bin/env python3

def calc(f, x, y):
    return f(x,y)

def add(x, y):
    return x + y

print(calc(add, 10, 20))
