#! /usr/bin/env python3

''' Given a list of numbers, and equations associated with each line,
    calculate a value for each line, and a sum of the results.
'''

def sumrange(row, arr, low, high):
    sum = 0
    for i in range(low, high+1):
        sum += arr[i]
    return sum

functions = [
        ( "Zero", lambda row, arr: ( 0 ) ),
        ( "sum of lines 1 - 8", lambda row, arr: sumrange(row, arr, 1, 8) ),
        ( "value of line 2", lambda row, arr: arr[row] ),
        ( "value of line 3", lambda row, arr: arr[row] ),
        ( "value of line 4", lambda row, arr: arr[row] ),
        ( "value of line 5", lambda row, arr: arr[row] ),
        ( "sum of lines 6 - 8", lambda row, arr: sumrange(row, arr, 6, 8) ),
        ( "line 7 + line 8", lambda row, arr: (arr[row]+arr[row+1]) ),
        ( "value of line 8", lambda row, arr: arr[row] ),
        ( "sum of lines 9 - 36", lambda row, arr: sumrange(row, arr, 9, 36) ),
        ( "line 10 + line 11", lambda row, arr: arr[row]+arr[row+1] ),
        ( "value of line 11", lambda row, arr: arr[row] ),
        ( "sum of lines 12 - 19", lambda row, arr: sumrange(row, arr, 12, 19) ),
        ( "value of line 13", lambda row, arr: arr[row] ),
        ( "value of line 14", lambda row, arr: arr[row] ),
        ( "sum of lines 15 - 19", lambda row, arr: sumrange(row, arr, 15, 19) ),
        ( "line 16 + line 17", lambda row, arr: arr[row]+arr[row+1] ),
        ( "value of line 17", lambda row, arr: arr[row] ),
        ( "line 18 + 19", lambda row, arr: arr[row]+arr[row+1] ),
        ( "value of line 19", lambda row, arr: arr[row] ),
        ( "sum of lines 20 - 31", lambda row, arr: sumrange(row, arr, 20, 31) ),
        ( "sum of lines 21 - 31", lambda row, arr: sumrange(row, arr, 21, 31) ),
        ( "value of line 22", lambda row, arr: arr[row] ),
        ( "value of line 23", lambda row, arr: arr[row] ),
        ( "sum of lines 24 - 28", lambda row, arr: sumrange(row, arr, 24, 28) ),
        ( "value of line 25", lambda row, arr: arr[row] ),
        ( "value of line 26", lambda row, arr: arr[row] ),
        ( "value of line 27", lambda row, arr: arr[row] ),
        ( "value of line 28", lambda row, arr: arr[row] ),
        ( "line 29 + 30", lambda row, arr: arr[29]+arr[30] ),
        ( "value of line 30", lambda row, arr: arr[row] ),
        ( "value of line 31", lambda row, arr: arr[row] ),
        ( "sum of lines 32 - 36", lambda row, arr: sumrange(row, arr, 32, 36) ),
        ( "sum of lines 33 - 36", lambda row, arr: sumrange(row, arr, 33, 36) ),
        ( "value of line 34", lambda row, arr: arr[row] ),
        ( "value of line 35", lambda row, arr: arr[row] ),
        ( "value of line 36", lambda row, arr: arr[row] ),
        ( "line 37 + 38", lambda row, arr: arr[37]+arr[38] ),
        ( "value of line 38", lambda row, arr: arr[row] ),
        ( "sum of lines 1 - 39", lambda row, arr: sumrange(row, arr, 1, 39) ),
        ]

values = [0, 0.72, 0.45, 0.52, 0.67, 1.2, 0.05, 0.69, 0.39, 6.14,
          1.87, 2.22, 1.98, 1.63, 0.35, 1.10, 0.73, 0.83, 1.10, 1.18,
          3.68, 6.28, 0.67, 1.11, 1.00, 0.43, 0.81, 0.40, 0.67, 0.40,
          0.20, 1.13, 9.14, 14.62, 0.67, 0.95, 0.16, 10.64, 0.63, 0.02,
          ]

sumvals = 0.0
sumfuncs = 0.0

if len(functions) != len(values):
    print("Problem with program: Length of the functions and values lists do not match. ({} - {})".format(len(functions), len(values)))

for i in range(1, len(functions)):
    val = functions[i][1](i, values)
    print("{:2} | {:5.2f} | {:20} | {:10.2f}".format(i, values[i], functions[i][0], val))
    sumvals += values[i]
    sumfuncs += val

print("-" * 46)
print("   | {:5.2f} | {:20} | {:10.2f}".format(sumvals, " ", sumfuncs))

