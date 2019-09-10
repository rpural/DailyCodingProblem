#! /usr/bin/env python3

''' 
    Test program to display colored text on the console
'''

def esc(code):
    return f'\033[{code}m'

print (esc('31;1;4') + 'really' + esc(0) + ' important')

