#! /usr/bin/env python3

import functools
import sys

print(sys.argv[1:])

sum = functools.reduce(lambda x,y: x+int(y), sys.argv[1:], 0)
print(sum)
