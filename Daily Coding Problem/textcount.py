#! /usr/bin/env python3
''' Daily Coding Problem

This problem was asked by Twitter.

Given a string, sort it in decreasing order based on the frequency of characters. 
If there are multiple possible solutions, return any of them.

For example, given the string tweet, return tteew. eettw would also be acceptable.
'''

from collections import Counter

def decreasing_occurances(text):
    occurances = Counter(text)
    result = ""
    for count, letter in sorted([(count, letter) for letter, count in occurances.items()], reverse=True):
        result += letter * count
    return result


if __name__ == "__main__":
    tweet = decreasing_occurances("tweet")
    print(f"tweet becomes {tweet}")
    anti = decreasing_occurances("antidisestablishmentism")
    print(f"andidisestablishmentism becomes {anti}")
    book = decreasing_occurances("bookkeeper")
    print(f"bookkeeper becomes {book}")
    inter = decreasing_occurances("internationalization")
    print(f"internationalization becomes {inter}")
