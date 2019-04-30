#! /usr/bin/env python3

'''
Create a program that will input a paragraph and the program will count
how many vowels, consonants are used, and what is the middle character
of the paragraph. In determining the middle character, disregard the 
spaces. If the character count is an even number, output "No middle
character", otherwise output the middle character.
'''

import re
import sys

text = sys.stdin.read()

print("Original text:")
print(text)
print()

newtext = re.sub(r'\s+', '', text)
newtext = newtext.lower()

if len(newtext) % 2 == 0:
    middle = None
else:
    mid = len(newtext) // 2
    middle = newtext[mid:mid+1]

vowel = 0
consonant = 0

for char in newtext:
    if char in "aeiou":
        vowel += 1

consonant = len(newtext) - vowel

print("Number of vowels: {}\nNumber of consonants: {}".format(vowel, consonant))
if middle:
    print("Middle character: {}".format(middle))
else:
    print("No middle character.")
