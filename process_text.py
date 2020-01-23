#! /usr/bin/env python3

''' Process a text file and count the occurances of the words '''

from collections import Counter
import re

with open("test.file", "r") as f:
    text = f.read()

text = re.sub(r"\s+", " ", text)
text = re.sub(r"[-.,%]+|'s", " ", text)

words = text.split(" ")

for i in range(len(words)):
    words[i] = words[i].lower().strip()

counts = Counter(words)

for word in sorted(counts.keys()):
    if word != "":
        print(f"{word:15}- {counts[word]}")
