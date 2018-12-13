#! /usr/bin/env python3

# Create a multiplication table for a given value, with a specified number
# of elements.

# Input the two variables
base = 5
count = 10

# The input will be text (strings), so convert the values to integers
base = int(base)
count = int(count)

# print a title for the table
print("\n\nMultiplication Table for", base)

# Loop through the count, starting at 0, and generate the table
for i in range(0, count+1):
    print(base, "times", i, "=", base * i)
