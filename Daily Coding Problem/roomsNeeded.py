#! /usr/bin/env python3

''' Daily Coding Challenge

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly 
overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

# sample: classTimes = [(30, 75), (0, 50), (60, 150)]
classTimes = list()

times = "-1"

while True:
    times = input("Enter the start and end times of a class (in minutes, such as 60,150): ")
    if times == "0":
        break
    timeBeginEnd = times.split(",")
    classTimes.append((int(timeBeginEnd[0]), int(timeBeginEnd[1])))

timelist = dict()

for (classStart, classEnd) in classTimes:
    print("start: {} end: {}".format(classStart, classEnd))

    for i in range(classStart, classEnd+1):
        timelist[i] = timelist.get(i, 0) + 1

rooms = 0

for i in timelist.values():
    if i > rooms:
        rooms = i

print("{} rooms needed.".format(rooms))
