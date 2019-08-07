#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In 
zigzag, characters are printed out diagonally from top left to bottom right 
until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

    t     a     g
     h   s z   a
       i i   i z
        s     g
'''

numberOfLines = 4
message = "thisisazigzag"

def zigzag(numberOfLines, message):
    cadance = numberOfLines * 2 - 1
    for i in range(numberOfLines):
