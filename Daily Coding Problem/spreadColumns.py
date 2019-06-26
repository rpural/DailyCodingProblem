#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., 
"AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, 
return "A". Given 27, return "AA".
'''

def base26(value):
    ''' Given a decimal value, return the base 26 column name for that value
    '''
    digits = list()

    while value > 0:
        digits.append( value % 26 )
        value //= 26

    result = ''
    while len(digits) > 0:
        digit = digits.pop()
        result = result + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[digit-1]
    return result


for test in (5, 25, 40, 127, 256, 1024):
    print("{} decimal converts to column {}".format(test, base26(test)))

