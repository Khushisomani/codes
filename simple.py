#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    l=[]
    k=n
    while(n>0):
        a=n%10
        l.append(a)
        n=n//10
    count=0
    for i in range(len(l)):
        if l[i]!=0:
            if k%l[i]==0:
                count+=1
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
