#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    s={}
    a=0
    for word in magazine:
        if word in s:
            s[word]+=1
        else:
            s[word]=1 
    for word in note:
        if word not in s.keys() or s[word]==0:
            a=1
            print('No')
            break
        else:
            s[word]-=1
    if a==0:
        print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
