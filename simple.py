#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n%2==1:
        k=n//2+1 
    else:
        k=n/2  
    if p<=k:
        page=p//2 
    else:
        a=n-p 
        page=a//2
    return(page)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
