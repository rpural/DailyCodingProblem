#! /usr/bin/env python3

def tripleUp1(nums):
    count = 0
    foo = False

    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            count += 1
        else:
            count = 0
    return count == 2


def tripleUp2(nums):
    count = 0
    foo = False

    for i in range(len(nums)):
        if i < len(nums)-1:
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                count = 0
        if count == 2:
            foo = True
    return foo

test = (1, 2, 3, 5, 6, 8, 9, 10, 12, 13)
print(tripleUp1(test))
print(tripleUp2(test))

