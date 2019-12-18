#! /usr/bin/env python3
'''
This program will print its name without any leading path
'''

import sys

program = sys.argv[0] # the full path of the program file

index = program.rfind("/") # the last index of a slash in the path
program = program[index+1:] # name is the next char to the end of the string

print(f"program name: {program}")
