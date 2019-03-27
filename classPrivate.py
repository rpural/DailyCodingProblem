#! /usr/bin/env python3

''' Test "private" variables within a Python Class '''

class A:
    def __init__(self):
        self._i = 1
        self.j = 5

    def display(self):
        print(self._i, self.j)


class B(A):
    def __init__(self):
        super().__init__()
        self._i = 2
        self.j = 8

c = B()
c.display()
