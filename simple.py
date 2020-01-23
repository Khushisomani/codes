#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    a=[]
    for i in range(len(p)):
        x=i+1 
        for j in range(len(p)):
            if p[j]==x:
                b=j+1
                for k in range(len(p)):
                    if p[k]==b:
                        a.append(k+1)
                        break
    return(a)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
