#! /usr/bin/env python3

''' Decimal to Binary

Print a table showing the powers of two in decimal, octal, hex and binary
'''

print("Powers of Two")
print(" ")
print("Decimal =   Hex   =  Octal  =     Binary")

for i in range(1, 17):
    print("{0:>7d} = {0:>7x} = {0:>7o} = {0:>18b}".format( 2 ** i ))

print(" ")
print("-----")
print(" ")
print("Powers of Two, minus 1")
print(" ")
print("Decimal =   Hex   =  Octal  =     Binary")

for i in range(1, 17):
    print("{0:>7d} = {0:>7x} = {0:>7o} = {0:>18b}".format( (2 ** i) - 1 ))

