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


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


cube = Cube(3)
print("surface area = {}, volume = {}".format(cube.surface_area(), cube.volume()))


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


pyr = RightPyramid(2, 4)
print("pyramid area = {}".format(pyr.area()))

