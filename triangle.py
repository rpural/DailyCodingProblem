#! /usr/bin/env python3

b = 34
c = 0
l = 0

while c < 33 :
    print(" " * b + "*" * c)
    b -= 1
    c += 2
    l += 1

print("line count = {}".format(l))
b = 34
c = 0
l = 0

while b > 0 and c < 33 :
    print(" " * b + "*" * c)
    b -= 1
    c += 2
    l += 1
print("line count = {}".format(l))
