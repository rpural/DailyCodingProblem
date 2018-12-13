#! /usr/bin/env python3

''' Multiplication Table

        Given a base number, and optionally a range, print a
        multiplication table for the base number, in a reasonable
        format.
'''

import sys

base = 0
count = 12

if len( sys.argv ) > 1:
    base = int( sys.argv[1] )
else:
    base = int( input( "Enter the base number for the table: " ))
    
if len( sys.argv ) > 2:
    count = int( sys.argv[2] )
    
print( "Multiplication Table for {}".format( base ))
print()

for i in range( 1, count + 1 ):
    print( "{:3} times {:3} equals {:6}".format( base, i, base * i ))