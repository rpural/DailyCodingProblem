#! /usr/bin/env python3

''' Daily Coding Problem
This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

In addition, note that the Roman numeral system uses subtractive notation for
numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
'''

numerals = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }

def romanDecode(xvi):
    xvi = xvi.upper()
    last = 0
    result = 0
    for n in xvi[::-1]:
        try:
            d = numerals[n]
        except:
            print("Found a non-Roman Numeral digit in the value submitted")
            return -1
        if d < last:
            result -= d
        else:
            result += d
            last = d
    return result

while True:
	roman = input("Input a value in Roman Numerals: ")
	if roman == "exit":
		break
	print("{} would be {}".format(roman, romanDecode(roman)))
