#! /usr/bin/python

import stack

# st = input("Enter a string to check for balanced symbols: ")

st = "()([])([{]})"

# Create a list of characters to be balanced, with the key being the closing 
# character, and the value being the expected opening character.
balance = { ")" : "(", "]" : "[", "}" : "{", ">" : "<", "'" : "'", '"' : '"' }

bal = stack.Stack()

# print("st = '{}'".format(st))
for c in st[:]:
    # print("at top, c = '{}'".format(c))
    if c in balance.keys():
        # print("stack = {}, peek = '{}'".format(bal._items, bal.peek()))
        o = bal.peek()
        # print("o = '{}'".format(o))
        if o != balance[c]:
            # print("o = '{}', c = '{}'".format(o, c))
            print("Unbalanced")
            exit()
        bal.pop()

    if c in balance.values():
        # print("at push, c = '{}'".format(c))
        bal.push(c)

if bal.is_empty():
    print("Balanced")
else:
    print("Unbalanced")

