#! /usr/bin/env python3

''' Test some unicode display points '''

up1 = "\u2160  \u2161  \u2162  \u2163  \u2164  \u2165  \u2166  \u2167"
up2 = "\u2168  \u2169  \u216A  \u216B  \u216C  \u216D  \u216E  \u216F"

dn1 = "\u2170  \u2171  \u2172  \u2173  \u2174  \u2175  \u2176  \u2177"
dn2 = "\u2178  \u2179  \u217A  \u217B  \u217C  \u217D  \u217E  \u217F"

for base in range(4096):
    characters = "\"{:03x}  - ".format(base)
    for i in range(base*16, base*16+16):
        characters += "\\u{:04x}  ".format(i)
    characters += "\""
    print(eval(characters))

