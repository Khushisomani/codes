#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    a=Counter()
    s=[]
    b=0
    for i in queries:
        if i[0]==1:
            a[i[1]]+=1
        elif i[0]==2:
            if i[1] in a and a[i[1]]>0: 
                a[i[1]]-=1 
        else:
            s.append(1 if i[1] in set(a.values()) else 0)
    return s
            

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
