#! /usr/bin/env python3

'''
    Find all the Palindromic numbers up to a given limit
'''

def isPalindromic(value):
    spal = str(value)
    if spal == spal[::-1]:
        return True
    else:
        return False


limit = int(input("Enter the upper limiting value: "))

count = 0
for i in range(limit + 1):
    if isPalindromic(i):
        count += 1
        print("{} is Palindromic".format(i))
print("Total: {}".format(count))
