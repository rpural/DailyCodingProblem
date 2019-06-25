#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of 
the pattern in the string. For example, given the string "abracadabra" and the 
pattern "abr", you should return [0, 7].
'''

import re

teststring = "abracadabra"
searchstring = "abr"

def matches(search, test):

    result = list()

    for match in re.finditer(search, test):
        result.append(match.start())

    return result

if __name__ == "__main__":
    print( matches( searchstring, teststring) )
