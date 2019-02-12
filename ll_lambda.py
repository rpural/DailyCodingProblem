#! /usr/bin/env python3

def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp - 32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    print(list(map(FahrenheitToCelsisus,ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    print(list(map(lambda f : (f - 32) * 5/9, ftemps)))
    print(list(map(lambda c : (c * 9/5) + 32, ctemps)))


if __name__ == "__main__":
    main()