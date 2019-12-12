#! /usr/bin/env python3

''' Example of using a coroutine to produce a simple running average
    over a set of numbers.
'''

def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == "__main__":
    avg = averager()
    next(avg)

    average = None
    while True:
        value = input("Enter a value, or 'end' to quit: ")
        if value.lower() == 'end':
            print(f"The final average was {average}")
            break
        average = avg.send(float(value))
        print(f"The running average is {average}.")
