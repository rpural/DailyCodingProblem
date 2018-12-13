#! /usr/bin/env python3

'''Daily Coding Problem

    This was a problem recently asked by Google during an interview:

    Accept a list of values and a target value. Return True if any two numbers
    in the list of values add up to the target value, otherwise return False.

    For example, given [10,15,3,7] and a target of 17, return True,
    since 10 + 7 = 17
'''

def checkList(target,valueList):
    ''' checkList(Target value, list of values)

        Solution presented here: 

        Given a target and a list of values return true if the first value
        plus any of the remaining values in the list add up to the target.
    
        Otherwise, remove the first value from the list, and call checkList()
        again to check the sums of the remaining values, until the list
        is empty
    '''
    if len(valueList) == 1:
        return False

    addend = valueList[0]
    for i in valueList[1:]:
        if (addend + i) == target:
            return True
    return checkList(target, valueList[1:])

listtext = input("Enter a list of numbers, separated by commas: ")

target = input("Enter a target sum: ")

values = listtext.split(",")

for i in range(len(values)):
    values[i] = int(values[i])

target = int(target)

print("list = {}, target = {}".format(values, target))

print(" result is {}".format( checkList(target, values) ))
