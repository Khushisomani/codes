# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:09:58 2020

@author: HP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if ar[i]==ar[j] and ar[j]!='a':
                count+=1 
                ar[j]='a'
                break
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
