#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Twitter.

You are given an array of length 24, where each element represents the number of 
new subscribers during the corresponding hour. Implement a data structure that 
efficiently supports the following:

    update(hour: int, value: int): Increment the element at index hour by value.
    query(start: int, end: int): Retrieve the number of subscribers that have 
        signed up between start and end (inclusive).

You can assume that all values get cleared at the end of the day, and that you 
will not be asked for start and end values that wrap around midnight.
'''

class hours:
    def __init__(self):
        self._hours = dict()

    def update(self, hour, v):
        self._hours[hour] = self._hours.get(hour, 0) + v

    def query(self, start, end):
        return [self._hours.get(h, 0) for h in range(start, end+1)]


if __name__ == "__main__":
    test = hours()

    test.update(5, 5)
    test.update(6, 3)
    test.update(8, 16)

    print("test query for hours 3 to 10: {}".format(test.query(3, 10)))
