#! /usr/bin/python

name = input('Enter your file name:')
print name
handle = open(name)

total = 0
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        total += 1
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print "Total:", total
print bigword, bigcount

