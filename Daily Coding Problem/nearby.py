#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].

'''

import math

def nearby(possibleslist, center, count):
    result = list()
    resultDist = list()

    for point in possibleslist:
        xsq = abs(center[0] - point[0])
        xsq *= xsq
        ysq = abs(center[1] - point[1])
        ysq *= ysq
        dist = math.sqrt(xsq + ysq)

        if len(resultDist) == 0:
            resultDist.append(dist)
            result.append(point)
        else:
            for (j, oldDist) in enumerate(resultDist):
                if oldDist > dist:
                    resultDist.insert(j, dist)
                    result.insert(j, point)
                    break
            else:
                resultDist.append(dist)
                result.append(point)

    return result[:count]

pointlist = [ (0, 0), (5, 4), (3, 1) ]

resultlist = nearby(pointlist, (1, 2), 2)
print(resultlist)
