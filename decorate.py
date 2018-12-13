#! /usr/bin/env python3

import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"debugging: {func.__name__}({signature})")
        ret = func(*args, **kwargs)
        print(f"end debugging: {func.__name__} returned {ret!r}")
        return ret
    return wrapper

@debug
def test_debugger(a, b):
    print("a = {}, b = {}".format(a, b))
    return a

c = test_debugger(1, 2)
print("c = {}".format(c))
