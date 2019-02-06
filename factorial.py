#! /usr/bin/env python3

'''
    Calculate factorials, in order to test several 
    theories and features.

    The first calculation method uses recursion, and a niave 
    approach, calculating the entire result each time.

    The second method uses the same recursion, but caches
    each answer in a large cache, such that once the sequence
    is known for any specific number, it is remembered, and 
    returned instead of recalculating the value.

    The third method removes the tail-recursion in favor
    of a for loop, using much less memory, and putting
    no pressure on the Python stack.
'''

import cache

faccache = cache.Cache(6000) # Enough to cover the entire problem space

def FactorialCached(value):
    if value <= 1:
        return 1

    cached = faccache.get(value)
    if cached != None:
        return cached

    fib = value * FactorialCached(value - 1)
    faccache.set(value, fib)
    return fib


def FactorialUncached(value):
    if value <= 1:
        return 1

    return value * FactorialUncached(value - 1)


def FactorialLoop(value):
    if value <= 1:
        return 1
    
    product = 1
    for i in range(2, value+1):
        product *= i

    return product


def FactorialLoopCached(value):
    if value <= 1:
        return 1

    product = 1
    for i in range(value, 1, -1):
        cached = faccache.get(i)
        if cached != None:
            product *= cached
            faccache.set(value, product)
            return product

        product *= i
    
    faccache.set(value, product)
    return product


import timer

import sys #, resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

n = 5000
#n = 10

with timer.Timer() as clock:
    for i in range(n):
        j = FactorialUncached(i)

print(f"Calculating the first {n} factorials, uncached: {clock.interval} seconds.")

with timer.Timer() as clock:
    for i in range(n):
        j = FactorialCached(i)

print(f"Calculating the first {n} factorials, cached: {clock.interval} seconds.")

faccache = cache.Cache(1000)

with timer.Timer() as clock:
    for i in range(n):
        j = FactorialCached(i)

print(f"Calculating the first {n} factorials, cache size 1000: {clock.interval} seconds.")

with timer.Timer() as clock:
    for i in range(n):
        j = FactorialLoop(i)

print(f"Calculating the first {n} factorials, tail-recusion unrolled: {clock.interval} seconds.")

# cache._debug_ = True

faccache = cache.Cache(6000)

with timer.Timer() as clock:
    for i in range(n):
        j = FactorialLoopCached(i)

print(f"Calculating the first {n} factorials, tail-recusion unrolled, cached: {clock.interval} seconds.") 

faccache = cache.Cache(1000)

with timer.Timer() as clock:
    for i in range(n):
        j = FactorialLoopCached(i)

print(f"Calculating the first {n} factorials, tail-recusion unrolled, cache size 1000: {clock.interval} seconds.") 
