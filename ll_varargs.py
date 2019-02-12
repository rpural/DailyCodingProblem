#! /usr/bin/env python3

def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))

    mynums = [5, 10, 15, 20]
    print(addition(*mynums))


if __name__ == "__main__":
    main()