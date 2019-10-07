#! /usr/bin/env python3

from fputs import fputs, StringTooShortError

x = fputs("This is a test file.", "test.file")

with open("test.file", "r") as f:
    print(f.read())

print(f"Created and displayed file of {x} bytes.")

try:
    x = fputs("short str", "test.file")
    with open("test.file", "r") as f:
        print(f.read())
    print(f"Created and displayed file of {x} bytes.")
except StringTooShortError as valerr:
    print(f"StringTooShortError: {valerr}")
