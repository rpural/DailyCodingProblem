#! /usr/bin/env python3

def main():

    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)
    
    s2 = b.decode('utf-8')
    print(s + s2)

    b2 = s.encode('utf-32')
    print(b+b2)

main()