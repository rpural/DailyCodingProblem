#! /usr/bin/env python3

# Create a multiplication table for a given value, with a specified number
# of elements.

def table(base, count):
    # print a title for the table
    print("\n\nMultiplication Table for", base)
    # Loop through the count, starting at 0, and generate the table
    for i in range(0, count+1):
        print(base, "times", i, "=", base * i)
    return 0

# Input the two variables
b = 5
c = 10

table(b, c)
