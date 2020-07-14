#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    l=[]
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            l.append(s[i])
        if s[i]=='}':
            if len(l)==0:
                return 'NO'
            popped=l.pop()
            if popped!='{':
                return 'NO'
        if s[i]==']':
            if len(l)==0:
                return 'NO'
            popped=l.pop()
            if popped!='[':
                return 'NO'
        if s[i]==')':
            if len(l)==0:
                return 'NO'
            popped=l.pop()
            if popped!='(':
                return 'NO'
    if len(l)!=0:
        return'NO'
    else:
        return 'YES'





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
