#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    count=0
    arr.sort()
    left=0
    right=1
    answer=0
    while right<len(arr):
        val=arr[right]-arr[left]
        if val==k:
            answer+=1
            left+=1
            right+=1
        elif val<k:
            right+=1 
        else:
            left+=1 
            if left==right:
                right+=1 
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
