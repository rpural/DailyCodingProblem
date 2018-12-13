#! /usr/bin/env python3

''' Daily Coding Problem #11
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of 
all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], 
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to 
speed up queries.
'''

querySet =  [ 'dog', 'deer', 'deal' ]

query = input("Enter query: ")

result = []

for i in querySet:
    if query == i[:len(query)]:
        result.append( i )

if len(result) == 0:
    print("No match found.")
elif len(result) == 1:
    print("match: {}".format(result[0]))
else:
    print("matches: {}".format(result))
