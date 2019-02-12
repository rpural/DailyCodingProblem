#! /usr/bin/env python3

class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


square = Square(4)
sq2 = Square(6)
print("area = {}, perimeter = {}".format(square.area(), square.perimeter()))
print("area = {}, perimeter = {}".format(sq2.area(), sq2.perimeter()))

