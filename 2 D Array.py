#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -9*7 + -1
    for i in range(4):
        for j in range(4):
            sum = 0
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum += arr[i+1][j+1]
            sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum > max_sum:
                max_sum = sum
                index = (i, j)
    return (max_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
