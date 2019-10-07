#! /usr/bin/env python3

from collections import Counter

input_list = [ 1, 2, 3, 1, 2, 1, 3, 1, 2, 1 ]

found = Counter()

found.update(input_list)

print( found )
