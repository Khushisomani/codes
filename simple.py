#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    a=100
    i=k
    while(i!=0):
        if c[i]==1:
            a=a-3 
        else:
            a=a-1
        if(i+k>len(c)-1):
            b=len(c)-i
            i=k-b
        else:
            i=i+k 
    if c[0]==0:
        a=a-1
    else:
        a=a-3
    return(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
