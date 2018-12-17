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
        lambda row, arr: ( 0 ),
        lambda row, arr: sumrange(row, arr, 1, 8),
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: sumrange(row, arr, 6, 8),
        lambda row, arr: (arr[7]+arr[8]),
        lambda row, arr: arr[row],
        lambda row, arr: sumrange(row, arr, 9, 36),
        lambda row, arr: arr[10]+arr[11],
        lambda row, arr: arr[row],
        lambda row, arr: sumrange(row, arr, 12, 19),
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: sumrange(row, arr, 15, 19),
        lambda row, arr: arr[16]+arr[17],
        lambda row, arr: arr[row],
        lambda row, arr: arr[18]+arr[19],
        lambda row, arr: arr[row],
        lambda row, arr: sumrange(row, arr, 20, 31),
        lambda row, arr: sumrange(row, arr, 21, 31),
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: sumrange(row, arr, 24, 28),
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[29]+arr[30],
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: sumrange(row, arr, 32, 36),
        lambda row, arr: sumrange(row, arr, 33,36),
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[row],
        lambda row, arr: arr[37]+arr[38],
        lambda row, arr: sumrange(row, arr, 1, 39),
        ]

values = [0, 0.72, 0.45, 0.52, 0.67, 1.2, 0.05, 0.69, 0.39, 6.14, 6.14,
          1.87, 2.22, 1.98, 1.63, 0.35, 1.10, 0.73, 0.83, 1.10, 1.18,
          3.68, 6.28, 0.67, 1.11, 1.00, 0.43, 0.81, 0.40, 0.67, 0.40, 0.20,
          1.13, 9.14, 14.62, 0.67, 0.95, 0.16, 10.64, 0.63, 0.02,
          ]

sumvals = 0.0
sumfuncs = 0.0

for i in range(1, len(functions)):
    val = functions[i](i, values)
    print("{:2} | {:5.2f} | {:10.2f}".format(i, values[i], val))
    sumvals += values[i]
    sumfuncs += val

print("-" * 17)
print("   | {:5.2f} | {:10.2f}".format(sumvals, sumfuncs))
