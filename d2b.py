#! /usr/bin/env python3

''' Conversions from decimal to / from binary '''

def to_binary(value):
    result = []
    while value > 0:
        result.append(value % 2)
        value //= 2

    return "".join([str(x) for x in reversed(result)])

def to_decimal(value):
    result = 0
    power = 1
    for i in reversed(value):
        result += int(i) * power
        power *= 2
    return result

if __name__ == "__main__":
    dectest = [ 5, 25, 42, 123456789 ]
    bintest = [ "101", "111", "10101010" "1100110011" ]

    print("Decimal to binary:")
    for i in dectest:
        print(f"{i} decimal = {to_binary(i)} binary")

    print("Binary to decimal:")
    for i in bintest:
        print(f"{i} binary = {to_decimal(i)}")

