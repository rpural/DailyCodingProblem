#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be 
initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the 
    cache and we are adding a new item, then it should also remove the least 
    frequently used item. If there is a tie, then the least recently used key 
    should be removed.

    get(key): gets the value at key. If no such key exists, return null.

    Each operation should run in O(1) time.
'''

_debug_ = False

class Cache:

    def __init__(self, size=100):
        if _debug_:
            print(f"debug: creating cache of size {size}")
        self._size = size
        self._values = dict()
        self._used = dict()
        self._usedtime = 0

    def set(self, key, value):
        if _debug_:
            print(f"debug: setting {key} to {value}")
        if str(key) in self._values:
            if _debug_:
                print(f"debug: found {key} in cache, usedtime = {self._usedtime}")
            self._values[str(key)] = value
            self._used[str(key)] = self._usedtime
            self._usedtime += 1
        else:
            if _debug_:
                print(f"debug: adding {key} with value {value}. usedtime = {self._usedtime}")
            if len(self._values) < self._size:
                if _debug_:
                    print(f"debug: Found unused space in cache")
                self._values[str(key)] = value
                self._used[str(key)] = self._usedtime
                self._usedtime += 1
            else:
                if _debug_:
                    print(f"debug: Finding oldest cache entry...")
                leastkey = -1
                leastused = -1
                if len(self._used) > 0:
                    for (k,u) in self._used.items():
                        if leastused == -1 or leastused > u:
                            leastused = u
                            leastkey = k
                    if _debug_:
                        print(f"debug: Oldest entry was {leastkey} at {leastused}")
                    del(self._values[leastkey])
                    del(self._used[leastkey])
                    self._values[str(key)] = value
                    self._used[str(key)] = self._usedtime
                    if _debug_:
                        print(f"debug: Adding {key} with value {value}, usedtime = {self._usedtime}")
                    self._usedtime += 1

    def get(self, key):
        if _debug_:
            print(f"debug: Fetching {key}")
        if str(key) in self._values:
            if _debug_:
                print(f"debug: Found {key} = {self._values[str(key)]}, old usedtime = {self._used[str(key)]}, new usedtime = {self._usedtime}")
            self._used[str(key)] = self._usedtime
            self._usedtime += 1
            return self._values[str(key)]
        else:
            return None

if __name__ == "__main__":

    _debug_ = True

    table = Cache(20)

    for i in (x for x in range(0,100)):
        table.set(i, i*2)
        j = table.get(i)
        j = table.get(0)

    if table.get(5) == None:
        print("5 no longer cached")
    else:
        print("err: 5 was cached")

    if table.get(92) == None:
        print("err: 92 wasn't cached")
    else:
        print("92 was cached")

    if table.get(0) == None:
        print("err: 0 wasn't cached, but should be")
    else:
        print("0 was cached")

    if table.get(500) == None:
        print("500 not found in cache, but was never added")
    else:
        print("err: 500 was found in the cache, but was never added")

