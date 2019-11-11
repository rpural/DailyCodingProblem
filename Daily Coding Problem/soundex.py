#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Grammarly.
Soundex is an algorithm used to categorize phonetically, such that two names 
that sound alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of one letter and three numbers, 
like M460.

One version of the algorithm is as follows:

Remove consecutive consonants with the same sound (for example, change ck -> c).
Keep the first letter. The remaining steps only apply to the rest of the string.
Remove all vowels, including y, w, and h.
Replace all consonants with the following digits:
b, f, p, v → 1
c, g, j, k, q, s, x, z → 2
d, t → 3
l → 4
m, n → 5
r → 6
If you don't have three numbers yet, append zeros until you do. Keep the first 
three numbers.

Using this scheme, Jackson and Jaxen both map to J250.

Implement Soundex.
'''

soundex_values = { "b" : 1, "f" : 1, "p" : 1, "v" : 1,
        "c" : 2, "g" : 2, "j" : 2, "k" : 2, "q" : 2, "s" : 2, "x" : 2, "z" : 2,
        "d" : 3, "t" : 3, "l" : 4, "m" : 5, "n" : 5, "r" : 6 ,
        "a" : 0, "e": 0, "i" : 0, "o" : 0, "u" : 0, "y" : 0,
        "h" : -1, "w" : -1 }


def soundex(name):
    work = str(name).lower()
    print(f"work: {work}")
    result = work[0:1]
    work = work[1:]
    print(f"work: {work}")

    for pos, ch in enumerate(work):
        print(f"work: {work}, pos: {pos}, ch: {ch}")
        value = soundex_values[ch]
        if value > 0 and pos > 0:
            if value != soundex_values[work[pos-1:pos]]:
                result += str(value)
            if len(result) == 4:
                return result
        elif value == -1:
            if pos > 0:
                if soundex_values[work[pos-1:pos]] == soundex_values[work[pos+1:pos+2]]:
                    work[pos+1:pos+2] = 'a'
    
    while len(result) < 4:
        result += "0"
    return result


if __name__ == "__main__":
    test = ""
    while True:
        test = input("Enter a name, or 'end' to quit: ").rstrip()
        if test == "end":
            break
        test_result = soundex(test)
        print(f"Soundex for {test} is {test_result}")
