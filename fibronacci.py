#! /usr/bin/env python3

'''
    Calculate the Fibronacci sequence, in order to test several 
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

fibcache = cache.Cache(6000) # Enough to cover the entire problem space

def FibronacciCached(value):
    if value <= 1:
        return 1

    cached = fibcache.get(value)
    if cached != None:
        return cached

    fib = value * FibronacciCached(value - 1)
    fibcache.set(value, fib)
    return fib


def FibronacciUncached(value):
    if value <= 1:
        return 1

    return value * FibronacciUncached(value - 1)


def FibronacciLoop(value):
    if value <= 1:
        return 1
    
    product = 1
    for i in range(2, value+1):
        product *= i

    return product


def FibronacciLoopCached(value):
    if value <= 1:
        return 1

    product = 1
    for i in range(value, 1, -1):
        cached = fibcache.get(i)
        if cached != None:
            product *= cached
            fibcache.set(value, product)
            return product * cached

        product *= i
    
    fibcache.set(value, product)
    return product


import timer

import sys #, resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

n = 5000
#n = 10

with timer.Timer() as clock:
    for i in range(n):
        j = FibronacciUncached(i)

print(f"Calculating the first {n} Fibronacci values, uncached: {clock.interval} seconds.")

with timer.Timer() as clock:
    for i in range(n):
        j = FibronacciCached(i)

print(f"Calculating the first {n} Fibronacci values, cached: {clock.interval} seconds.")

fibcache = cache.Cache(1000)

with timer.Timer() as clock:
    for i in range(n):
        j = FibronacciCached(i)

print(f"Calculating the first {n} Fibronacci values, cache size 1000: {clock.interval} seconds.")

with timer.Timer() as clock:
    for i in range(n):
        j = FibronacciLoop(i)

print(f"Calculating the first {n} Fibronacci values, tail-recusion unrolled: {clock.interval} seconds.")

# cache._debug_ = True

fibcache = cache.Cache(6000)

with timer.Timer() as clock:
    for i in range(n):
        j = FibronacciLoopCached(i)

print(f"Calculating the first {n} Fibronacci values, tail-recusion unrolled, cached: {clock.interval} seconds.") 

fibcache = cache.Cache(1000)

with timer.Timer() as clock:
    for i in range(n):
        j = FibronacciLoopCached(i)

print(f"Calculating the first {n} Fibronacci values, tail-recusion unrolled, cache size 1000: {clock.interval} seconds.") 