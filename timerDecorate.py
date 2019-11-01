#! /usr/bin/env python3
''' Implement a timer decorator to time the execution of a function '''

import time
from functools import lru_cache

def timer(fmt="[{elapsed:0.8f}s] {name}({args}) -> {result}"):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


if __name__ == "__main__":
    @timer()
    @lru_cache()
    def fibonacci(n):
        if n <= 1:
            return 1
        return fibonacci(n-1) + fibonacci(n-2)

x = fibonacci(11)
