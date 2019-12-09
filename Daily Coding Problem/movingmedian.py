#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Microsoft.

Given an array of numbers arr and a window of size k, print out the median of 
each window of size k starting from the left and moving right by one position 
each time.

For example, given the following array and k = 3:

    [-1, 5, 13, 8, 2, 3, 3, 1]
    Your function should print out the following:

    5 <- median of [-1, 5, 13]
    8 <- median of [5, 13, 8]
    8 <- median of [13, 8, 2]
    3 <- median of [8, 2, 3]
    3 <- median of [2, 3, 3]
    3 <- median of [3, 3, 1]
    Recall that the median of an even-sized list is the average of the two 
    middle numbers.
'''

def movingMedian(arr, k):
    ''' Print the median of values in arr, taken k elements at a time '''
    result = list()
    if k % 2 == 0:
        medianloc = k // 2 - 1
    else:
        medianloc = k // 2
    for i in range(len(arr)-k+1):
        sub = sorted(arr[i:i+k])
        if k % 2 == 0:
            result.append((sub[medianloc]+sub[medianloc+1])/2)
        else:
            result.append(float(sub[medianloc]))
    return result


if __name__ == "__main__":
    test1 = [-1, 5, 13, 8, 2, 3, 3, 1]
    print(f"test array = {test1}")
    result1 = movingMedian(test1, 3)
    result2 = movingMedian(test1, 4)
    result3 = movingMedian(test1, 5)

    print("k = 3:")
    for i in range(len(test1) - 3 + 1):
        print(f"{result1[i]} - median of {test1[i:i+3]}")
    print("k = 4:")
    for i in range(len(test1) - 4 + 1):
        print(f"{result2[i]} - median of {test1[i:i+4]}")
    print("k = 5:")
    for i in range(len(test1) - 5 + 1):
        print(f"{result3[i]} = median of {test1[i:i+5]}")
