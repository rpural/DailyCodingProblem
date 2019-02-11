#! /usr/bin/env python3

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x.islower():
        return True
    return False


def squareFunc(x):
    return x ** 2


def toGrade(x):
    if (x >= 90):
        return "A"
    if 80 < x < 90:
        return "B"
    if 70 < x <= 80:
        return "C"
    if 60 < x <= 70:
        return "D"
    return "F"
    


def main():
    # define some sample sequences to operate on
    nums = ( 1, 8, 4, 5, 13, 26, 381, 410, 58, 47 )
    chars = "abcDeFGHiJKlmnoP"
    grades = ( 81, 89, 94, 78, 61, 66, 99, 74 )

    odds = list( filter(filterFunc, nums) )
    print(odds)

    lowers = list( filter(filterFunc2, chars))
    print(lowers)
    
    squares = list( map(squareFunc, nums) )
    print(squares)

    grades = sorted(grades)
    letters = list( map(toGrade, grades) )
    print( letters )

if __name__ == "__main__":
    main()
