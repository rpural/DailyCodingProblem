#! /usr/bin/env python3

from timer import Timer
import re

re_pattern_1 = r"^\w"
re_pattern_2 = r"^."

search_string = "Now is the time for all good men to..."
print("search string: '{}'".format(search_string))

print("Search pattern 1 yields: {}".format(re.match(re_pattern_1, search_string).group()))
print("Search pattern 2 yields: {}".format(re.match(re_pattern_2, search_string).group()))
print("Slicing yields: {}".format(search_string[:1]))

iterations = 1_000_000
print("\nTimes for {} executions:\n".format(iterations))

with Timer() as t:
    for _ in range(iterations):
        c = re.match(re_pattern_1, search_string).group()

print("Search pattern 1 time: {:5.03f}".format(t.interval))

with Timer() as t:
    for _ in range(iterations):
        c = re.match(re_pattern_2, search_string).group()

print("Search pattern 2 time: {:5.03f}".format(t.interval))

with Timer() as t:
    for _ in range(iterations):
        c = search_string[:1]

print("Slicing time: {:5.03f}".format(t.interval))
