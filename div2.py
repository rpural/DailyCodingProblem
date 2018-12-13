#! /usr/bin/env python3

x = 19

while x > 1:
    y = x % 2
    x = x // 2
    print("y = ", y)

print("x = ", x)
