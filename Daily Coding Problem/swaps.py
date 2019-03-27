#! /usr/bin/env python3

''' Daily Coding Problem

    This problem was asked by Cisco.

    Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped,
    the 3rd and 4th bit should be swapped, and so on.

    For example, 10101010 should be 01010101. 11100010 should be 11010001.

    Bonus: Can you do this in one line?
'''

bin1 = "10101010"  #  should be 01010101 
bin2 = "11100010"  #  should be 11010001

def swaps(bitmap):
    result = ""
    
    while len(bitmap) > 0:
        result +=  bitmap[1:2] + bitmap[:1]
        bitmap = bitmap[2:]

    return result

print("{} swapped = {}".format(bin1, swaps(bin1)))
print("{} swapped = {}".format(bin2, swaps(bin2)))



