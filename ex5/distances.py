#! /usr/bin/env python3

import numpy as np

def find_distance(filename, city1, city2):
    table = np.loadtxt(filename, delimiter=",")
    return table[city1, city2]

if __name__ == "__main__":
    print("from 1 to 3:", find_distance("distances.txt", 1, 3))
    print("from 0 to 2:", find_distance("distances.txt", 0, 2))
    print("from 0 to 3:", find_distance("distances.txt", 0, 3))
    print("from 0 to 1:", find_distance("distances.txt", 0, 1))
    print("from 1 to 0:", find_distance("distances.txt", 1, 0))

