#! /usr/bin/env python3

from enum import Enum

class Fruit(Enum):
   APPLE = 1
   BANANA = 2
   ORANGE = 3
   TOMATO = 4

def main():
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))


if __name__ == "__main__":
    main()