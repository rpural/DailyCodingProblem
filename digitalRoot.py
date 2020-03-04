#! /usr/bin/env python3

from functools import reduce

def digitalRoot(value):
    if value < 10:
        return value
    root = [ int(x) for x in str(value) ]
    return digitalRoot(reduce(lambda x,y: x + y, root))


if __name__ == "__main__":
    tests = [45893, 42, 956, 953, 21]
    for value in tests:
        print(f"digital root of {value} is {digitalRoot(value)}, calculated via mod is {value%9}")
