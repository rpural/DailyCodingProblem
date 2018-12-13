#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes i
the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node == None:
        return ""
    return "-v:" + node.val + "-l:" + node.val + ":" + serialize(node.left) + "-r:" + node.val + ":" + serialize(node.right) + "--:" + node.val


def deserialize(string):
    node = None
    if string == "":
        return node
    match = re.match("^-v:(.+?)-l:\\1:(.*)-r:\\1:(.*)--:\\1", string)
    if match == None:
        print("string didn't match pattern: {}".format(string))
    # print("\tdeserialize: v:{} l:{} r:{}".format(match.group(1),match.group(2),match.group(3)))
    if match.group(2) != "":
        lnode = deserialize(match.group(2))
    else:
        lnode = None
    if match.group(3) != "":
        rnode = deserialize(match.group(3))
    else:
        rnode = None
    return Node(match.group(1), lnode, rnode)

node = Node('root', Node('left', Node('left.left')), Node('right'))

ser = serialize(node)
print("/{}/".format(ser))
if deserialize(ser).left.left.val == 'left.left':
    print("Serialize and deserialize worked")
else:
    print("Serialize or deserialize failed")
