#! /usr/bin/env python3

''' quicksort.py

        Implement a version of the QuickSort method
'''

def quicksort(original):

    if len(original) < 2:
        return original

    l = original

    pivot = 0
    head = 1
    tail = len(l) - 1

    try:
        while head <= tail and l[head] < l[pivot]:
            head += 1
        while head <= tail and l[tail] > l[pivot]:
            tail -= 1

        if l[head] > l[tail]:
            (l[head], l[tail]) = (l[tail],l[head])
        (l[head], l[pivot]) = (l[pivot], l[head])
    except IndexError:
        print("Index error:")
        lngth = len(l)
        print(f"len(list) = {lngth}, head = {head}, tail = {tail}, pivot = {pivot}")

    lhead = list(l[:head])
    ltail = list(l[tail:])
    try:
        l = quicksort(lhead) + [l[head]] + quicksort(ltail)
    except RecursionError:
        print(f"list = {l}, head  = {head}, tail = {tail}, pivot = {pivot}\nlhead = {lhead}, head = {l[head]}, ltail = {ltail}")

    return l


inlist = [ 25, 6, 2, 4, 42, 97, 3, 2, 1 ]

print(inlist)
print(quicksort(inlist))
print(inlist)
