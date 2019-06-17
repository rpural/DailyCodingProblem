#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
'''

searchlist1 = [5, 7, 10, 3, 4]

searchlist2 = [22, 31, 35, 43, 48, 56, 61, 70, 75, 80, 81, 82, 2, 4, 6, 8, 10, 12, 16, 21]

def searchmin(searchlist):
    # set the initial lower and upper bound for the search
    lb, ub = 0, len(searchlist)
    val = searchlist[0]  # seed the found value
    compares = 0

    while True:
        mid = lb + (ub - lb) // 2
        compares += 1
        if searchlist[mid] < val:
            # this would be above the rotation point
            ub = mid
            if searchlist[mid] < searchlist[mid-1]:
                if __name__ == "__main__":
                    print("  (compares = {})".format(compares))
                return searchlist[mid]  # found
            val = searchlist[mid]
        else:
            # this would be below the rotation point
            lb = mid

if __name__ == "__main__":
    print(searchlist1)
    print(searchmin(searchlist1))
    print("---")
    print(searchlist2)
    print(searchmin(searchlist2))
    for _ in range(3):
        v = searchlist2.pop()
        searchlist2.insert(0, v)
    print("---")
    print(searchlist2)
    print(searchmin(searchlist2))
    for _ in range(3):
        v = searchlist2.pop()
        searchlist2.insert(0, v)
    print("---")
    print(searchlist2)
    print(searchmin(searchlist2))
    for _ in range(5):
        v = searchlist2.pop()
        searchlist2.insert(0, v)
    print("---")
    print(searchlist2)
    print(searchmin(searchlist2))


