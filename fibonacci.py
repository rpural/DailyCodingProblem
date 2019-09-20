#! /usr/bin/env python3

''' 
    Various ways of generating the fibonacci sequence
'''
def fibonacci1(n):
  # Taken from "30 Seconds of Python",
  # http:github.com/30-seconds/30-seconds-of-python
  if n <= 0:
    return [0]

  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)

  return sequence


class fibonacci2:
    def __init__(self):
        self.previous = []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.previous) == 0:
            self.previous.append(0)
            return 0
        elif len(self.previous) == 1:
            self.previous.append(1)
            return 1
        else:
            self.previous.append(self.previous[0] + self.previous[1])
            self.previous.pop(0)
            return self.previous[1]


def fibonacci3(n):
    previous = [0]
    yield 0
    while n > previous[-1]:
        if len(previous) == 0:
            previous.append(0)
            yield 0
        elif len(previous) == 1:
            previous.append(1)
            yield 1
        else:
            previous.append(previous[0] + previous[1])
            previous.pop(0)
            yield previous[1]


print(fibonacci1(10))

fib = fibonacci2()
print([fib.next() for x in range(11)])

print(list(fibonacci3(55)))

