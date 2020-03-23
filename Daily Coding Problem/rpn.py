#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to 
evaluate it.

The expression is given as a list of numbers and operands. 
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
'''

import operator

def rpn(equation):
    ops = {'+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': operator.floordiv}
    stack = []
    p = 0  # position in string
    l = 1  # length of operand

    while p < len(equation):
        if equation[p].isnumeric():
            while equation[p:p+l].isnumeric():
                l += 1
            l -= 1
            value = int(equation[p:p+l])
            stack.append(value)
            p += l
            l = 1
        elif equation[p] in "+-*/":
            op1 = stack.pop()
            op2 = stack.pop()
            value = ops[equation[p]](op2, op1)
            stack.append(value)
            p += 1
        elif equation[p] == " ":
            p += 1
        else:
            print(f"Invalid equation at {p}: {equation[p:]}")
            break
    return stack[0]


if __name__ == "__main__":
    while True:
        equation = input("Enter your equation in Reverse Polish Notation (operator or space between numerics):")
        if len(equation) == 0 or equation == "":
            break

        result = rpn(equation)
        print(f"result = {result}")
