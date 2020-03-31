#! /usr/bin/env python3

''' Check an input to see if it qualifies as a strong password.
    
    A strong password is at least 8 characters long, contains both upper
    and lower case characters, and has at least one digit. (not my definition)

    The original description said that you might need to use more than one
    regular expression to check the conditions. I wanted to see if I could
    do it with a single regular expression.
'''

import re

pswd = re.compile(r"(?=.{8})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])")
# First, check that the password is at least 8 characters long
# Then, check that there is at least one lower case character
# Then, check that there is at least one Upper case character
# Then, check that there is at least one number
# These are all done via lookaheads, so the actual cursor is still sitting
# at the beginning of the string. Additional checks could be done from there.

test = input("Password: ")
if pswd.search(test):
    print("Passed")
else:
    print("Failed")
