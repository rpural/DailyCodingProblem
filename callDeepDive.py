#! /usr/bin/env python3

class Prefixer:
    def __init__(self, prefix):
        self.prefix = prefix
    def __call__(self, message):
        return self.prefix + message

ick = Prefixer("ICKDSF: ")

print(ick("This is a test message"))

def increment(x):
    return x + 1

print( increment.__call__(2))
