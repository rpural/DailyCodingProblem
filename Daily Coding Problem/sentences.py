#! /usr/bin/env python3

''' Daily Coding Challenge

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

words = [ 'quick', 'brown', 'the', 'fox', 'jumped', 'lazy', 'dog', 'over', 'lazydog' ]

sentence = 'thequickbrownfoxjumpedoverthelazydog'
sentences = list()

def checkSentence(sentence, position, workinglist=[]):
    if len(sentence) == position:
        print("complete match: {}".format(workinglist))
        sentences.append(workinglist.copy())
    else:
        partialSentence = sentence[position:]
        for i in words:
            if partialSentence[0:len(i)] == i:
                workinglist.append(i)
                print("partial match: {} - {}".format(sentence[0:position+len(i)], workinglist))
                print("next call: {}, {} {}".format(position, sentence[0:position+len(i)], sentence[position+len(i):]))
                checkSentence(sentence, position+len(i), workinglist)
                workinglist.pop()
    return

print(sentence)
print(words)
print()
checkSentence(sentence, 0)

print()
print("Solutions:")
for i in sentences:
    print("   {}".format(i))
