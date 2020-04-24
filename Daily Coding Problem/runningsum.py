#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
'''

def findSum(lst, target, sum_=0, begin=0, current=0):
    ''' Find a set of consecutive values in lst that sum up to target '''

    if sum_ + lst[current] == target:
        return lst[begin:current+1]

    if sum_ + lst[current] > target:
        return None

    sum_ += lst[current]
    current += 1
    if current == len(lst):
        return None

    result = findSum(lst, target, sum_, begin, current)

    if result:
        return result

    while result is None:
        begin += 1
        if begin == len(lst):
            return None
        sum_ = 0
        current = begin
        result = findSum(lst, target, sum_, begin, current)
        if result:
            return result
    return None

if __name__ == "__main__":
    samples = [[[1,2,3,4,5], 9],
               [[1,2,3,4,5], 8],
               [[1,2,3,4,5], 12]
              ]

    for l, t in samples:
        print(f"list: {l}, target: {t} - Result: {findSum(l, t)}")
