#! /usr/bin/env python3

import collections


def main():
    Point = collections.namedtuple("Point", "x y")

    p1 = Point(10, 20)
    p2 = Point(5, 8)

    print(p1, p2)
    print(p1.x, p2.y)

    p1 = p1._replace(x=100)
    print(p1)


    class1 = ["Bob", "Becky", "Frank", "Charlie", "James", "Darcy", "James", "Chad"]

    class2 = ["Bill", "Berry", "Cindy", "Debbie", "Frank"]

    c1 = collections.Counter(class1)
    c2 = collections.Counter(class2)

    print(sum(c1.values()))
    print(c1.most_common(3))

    print(c1 & c2)


    import string

    d = collections.deque(string.ascii_lowercase)
    print(len(d))

    for elem in d:
        print(elem, end=", ")
    print()

    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)

    print(d)

    d.rotate(5)
    print(d)

    d.rotate(-6)
    print(d)


if __name__ == "__main__":
    main()