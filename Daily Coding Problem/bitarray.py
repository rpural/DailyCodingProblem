#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
'''

class Bitarray:
    def __init__(self, size):
        self._array = [ 0 for i in range(size//8) ]

    def get(self, index):
        pit = index // 8
        bit = 1 << (index % 8)

        if self._array[pit] & bit:
            return 1
        else:
            return 0

    def set(self, index, val=1):
        pit = index // 8
        bit = 1 << (index % 8)

        if val == 1:
            self._array[pit] = self._array[pit] | bit
        else:
            self._array[pit] = self._array[pit] & (7 - bit)


if __name__ == "__main__":
    x = Bitarray(25)

    print(x._array)

    x.set(8)

    print(x._array)

    x.set(10)

    print(x._array)

    x.set(8, 0)

    print(x._array)

    x.set(4,1)
    x.set(18,1)

    print(x._array)
