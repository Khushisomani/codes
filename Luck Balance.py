#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    l=[]
    luck=0
    for i in range(len(contests)):
        if contests[i][1]==1:
            l.append(contests[i][0])
        else:
            luck+=contests[i][0] 
    l.sort(reverse=True)
    for i in range(len(l)):
        if k>0:
            luck+=l[i]
            k-=1 
        else:
            luck-=l[i]
    return luck
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
