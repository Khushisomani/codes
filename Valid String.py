#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d={}
    count=[]
    for i in s:
        if i in d:
            d[i]+=1 
        else:
            d[i]=1 

    for i in d:
        count.append(d[i])
    a=1
    b=count[0]
    for i in range(1,len(count)):
        if b==count[i]:
            continue
        else:
            a-=1 
    if a>=0:
        return 'YES'
    else:
        return 'NO'
        


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
