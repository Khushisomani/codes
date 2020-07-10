#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    a=1
    for i in range(len(q)):
        if (q[i] - (i + 1) > 2):
            print("Too chaotic")
            a=0
            break            
        for j in range(i):
            if (q[j] > q[i]):
                bribes+=1
    if a==1:
        print(bribes)
  

    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
