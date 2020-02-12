#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Apple.

Implement a queue using two stacks. 

Recall that a queue is a FIFO (first-in, first-out) data structure with the 
following methods: enqueue, which inserts an element into the queue, and 
dequeue, which removes it.
'''

# First, a quick implementation of a stack

class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return None

    def __str__(self):
        return f"{self.stack}"


# implement a fifo queue using two stacks for data storage
class Queue:
    def __init__(self):
        # allocate two stacks
        self.stacks = [Stack(), Stack()]
        self.direction = 0 # if zero, last added to the queue, one if dequeueing

    def _reverse(self):
        source = self.direction
        target = 0 if self.direction else 1

        value = self.stacks[source].pop()
        while value != None:
            self.stacks[target].push(value)
            value = self.stacks[source].pop()

        self.direction = target

    def enqueue(self, value):
        if self.direction: # if we were dequeueing, reverse the stacks, then add
            self._reverse()
        self.stacks[self.direction].push(value)

    def dequeue(self):
        if not self.direction: # if we were enqueueing, reverse the stacks, then retrieve
            self._reverse()
        return self.stacks[self.direction].pop()

    def __str__(self):
        if self.direction: # print in the order the values will be dequeued
            self._reverse()
        return f"Queue: {self.stacks[self.direction]}"


if __name__ == "__main__":
    que = Queue()

    print(que)
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    print(que)
    print(que.dequeue())
    print(que.dequeue())
    print(que)
    que.enqueue(5)
    que.enqueue(6)
    print(que)
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())
    print(que)
