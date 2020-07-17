#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    b=[i%2 for i in B]
    c=0
    for i in range(len(b)-1):
        if b[i] and b[i+1]:
            b[i]=0
            b[i+1]=0
            c+=1 
        elif b[i] and not b[i+1]:
            b[i]=0
            b[i+1]=1
            c+=1 
    return 'NO' if any(b) else c*2
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
