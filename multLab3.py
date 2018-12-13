#! /usr/bin/env python3

# Create a multiplication table for a given value, with a specified number
# of elements.

def table(base, count):
    # print a title for the table
    print("\n\nMultiplication Table for", base)

    # Loop through the count, starting at 0, and generate the table
    for i in range(0, count+1):
        print(base, "times", i, "=", base * i)


# Input the two variables
base = input("Create a multiplication table for what value: ")
count = input("Number of elements in the table: ")

# The input will be text (strings), so convert the values to integers
try:
    base = int(base)
    count = int(count)
except ValueError:
    print("The program expects integers for the two values.")
    print("Re-run and enter integer numbers at the two prompts.")
    exit(1)

table(base, count)
