#! /usr/bin/env python3

ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 21]

evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Creating a list using map and filter
evenSquared = list(map(lambda e: e**2, filter(lambda e: 4 < e < 16, evens)))
print(evenSquared)

# Creating the same list using comprehensions
evenSquared = [e**2 for e in evens if 4 < e < 16]
print(evenSquared)

# Dictionary list comprenhension
tempDict = { t: (t * 9/5) + 32 for t in ctemps }
print(tempDict)

# Set comprehension example
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

ftemps1 = [ (t * 9/5) + 32 for t in ctemps ]
ftemps2 = { (t * 9/5) + 32 for t in ctemps }

print(ftemps1)
print(ftemps2)

sChars = "The quick brown fox jumped over the lazy dog"
chars = { c.upper() for c in sChars if not c.isspace() }
print(chars)
