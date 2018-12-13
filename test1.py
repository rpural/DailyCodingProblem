#! /usr/bin/python

total = 0.0

for i in range(11):
    value = float(input("Enter a value (0.0 to end):"))
    if value == 0.0:
        break
    total += value
print "The total is", total

exit(0)

