#! /usr/bin/env python3

''' An Armstrong number is one where the sum of the cubes of the digits add
    up to the number itself. Example 371 = 3**3 + 7**3 + 1**3.
'''

def isArmstrong(value):
    svalue = str(value)
    digits = len(svalue)
    sum = 0
    for i in svalue:
        sum += int(i) ** digits
    if sum == value:
        return True
    else:
        return False


limit = int(input("Input the end of the desired range: "))
count = 0
for i in range(limit+1):
    if isArmstrong(i):
        count += 1
        print("{}. {} is an Armstrong number.".format(count, i))
print("Total found: {}".format(count))
