#! /usr/bin/env python3

''' Daily Coding Problem

Let's represent an integer in a linked list format by having each node represent 
a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

    1 -> 2 -> 3 -> 4 -> 5
    is the number 54321.

    Given two linked lists in this format, return their sum in the same linked 
    list format.

    For example, given

    9 -> 9
    5 -> 2
    return 124 (99 + 25) as:

    4 -> 2 -> 1
'''

def toNumberList(value):
    result = []
    while value > 0:
        result.append(value % 10)
        value //= 10
    return result


def fromNumberList(lst):
    result = 0
    for digit in lst[::-1]:
        result = result * 10 + digit
    return result


def addNumberList(lst1, lst2):
    if len(lst1) > len(lst2):
        lsta = list(lst1)
        lstb = list(lst2)
    else:
        lsta = list(lst2)
        lstb = list(lst1)

    while len(lstb) < len(lsta):
        lstb.append(0)

    lsta.append(0)

    for i in range(len(lstb)):
        temp = lsta[i] + lstb[i]
        if temp > 9:
            lsta[i] = temp % 10
            lsta[i+1] += temp // 10
        else:
            lsta[i] = temp

    if lsta[-1] == 0:
        del lsta[-1]

    return lsta


if __name__ == "__main__":
    t1 = toNumberList(99)
    t2 = toNumberList(25)
    t3 = addNumberList(t1, t2)
    print(f"{t1} +  {t2} = {t3}")

    t1 = toNumberList(716354)
    t2 = toNumberList(942257392)
    t3 = addNumberList(t1, t2)
    print(f"{t1} +  {t2} = {t3}")
    print(f"{fromNumberList(t1)} + {fromNumberList(t2)} = {fromNumberList(t3)}")

