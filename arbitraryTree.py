#! /usr/bin/env python3

''' Implement a self-defining tree of arbitrary but finite size '''

import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right

        self._is_left_evaluated = False
        self._is_right_evaluated = False


    @property
    def left(self):
        if not self._is_left_evaluated:
            if random.random() < 0.5:
                self._left = Node(0)

        self._is_left_evaluated = True
        return self._left

    @property
    def right(self):
        if not self._is_right_evaluated:
            if random.random() < 0.5:
                self._right = Node(0)

        self._is_right_evaluated = True
        return self._right

def generate():
    return Node(0)

def walk(tree, count=0):
    count +=1
    ltr = tree.left
    if ltr:
        count = walk(ltr, count=count)
    rtr = tree.right
    if rtr:
        count = walk(rtr, count=count)
    return count

tr = generate()

# Walk the tree and count the nodes

count = walk(tr)

print("nodes = {}".format(count))


