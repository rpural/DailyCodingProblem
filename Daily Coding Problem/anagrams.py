#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Robinhood.

Given an array of strings, group anagrams together.

For example, given the following array:

    ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    Return:

    [['eat', 'ate', 'tea'],
     ['apt', 'pat'],
     ['now']]
'''

def anagrams(list_of_words):
    unique_letters = dict()

    for word in list_of_words:
        work = sorted(word)
        letters = "".join(work)
        try: 
            unique_letters[letters].append(word)
        except KeyError:
            unique_letters[letters] = [word]

    #result = []
    #for word_list in unique_letters.values():
    #    result.append(word_list)

    #return result
    return [word_list for word_list in unique_letters.values()]

if __name__ == "__main__":
    test_list = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    print(anagrams(test_list))

