#! /usr/bin/env python3

def isPerfectNumber(integer):
    divisors = []
    for i in range(1, integer // 2 + 1):
        if integer % i == 0:
            divisors.append(i)
    sumDiv = sum(divisors)
    if sumDiv == integer:
        return True
    else:
        return False


for test in (504, 6, 12):
    if isPerfectNumber(test):
        print("{} is a perfect number.".format(test))
    else:
        print("{} is not a perfect number.".format(test))

for test in range(1, 100000):
    if isPerfectNumber(test):
        print("Found perfect number {}".format(test))
