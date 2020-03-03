#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three 
colors: red, green, and blue. One power of the Qux is that if two of them are 
standing next to each other, they can transform into a single creature of the 
third color.

Given N Quxes standing in a line, determine the smallest number of them remaining 
after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end 
up with a single Qux through the following steps:

            Arrangement       |   Change
            ----------------------------------------
            ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
            ['B', 'B', 'G', 'B']      | (B, G) -> R
            ['B', 'R', 'B']           | (R, B) -> G
            ['B', 'G']                | (B, G) -> R
            ['R']                     |
'''            

def qux(quxlist):
    quxl = list(quxlist)
    conversions = {"RG": "B", "RB": "G", "BG": "R",
                   "GR": "B", "BR": "G", "GB": "R"}

    p = 0
    while True:
        if p < len(quxl) - 1:
            comb = quxl[p] + quxl[p+1]
            if comb in conversions:
                quxl[p] = conversions[comb]
                del quxl[p+1]
                p = -1
        else:
            break
        p += 1
        if p == len(quxl):
            break

    return quxl


if __name__ == "__main__":
    q = [ ['R', 'G', 'B', 'G', 'B'],
          ("R", "G", "R", "G", "B"),
          ['G', 'G', 'G', 'R', 'G', 'B', 'G', 'R'],
          [x for x in 'RGBRGBRGB'] ]

    for query in q:
        result = qux(query)
        print(f"original: {query}, result: {result}")
