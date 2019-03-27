#! /usr/bin/env python3

''' Find the longest matching string at the beginning and end of a given string
'''

import re

string = input("Enter a sting: ")

match = re.match( r"^(.+).*\1$", string )
if match:   print( "matching string: {}".format(match.group(1)) )
else:       print( "no match" )
