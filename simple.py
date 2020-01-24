#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l=[]
    l.append(len(arr))
    while len(arr)!=0:
        a=min(arr)
        for j in range(len(arr)):
            arr[j]=arr[j]-a
        b=arr.count(0)
        for i in range(b):
            arr.remove(0)
        l.append(len(arr))
    l.remove(0)
    return(l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
