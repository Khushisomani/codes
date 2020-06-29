#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter
if __name__ == '__main__':
    l={}
    s = input()
    for i in s:
        l[i]=s.count(i)
    d_sort=sorted(l.items(),key=lambda x:x[1],reverse=True)
    for i in range(3):
        if d_sort[i][1]==d_sort[i+1][1]:
            if d_sort[i][0]>d_sort[i+1][0]:
                d_sort[i],d_sort[i+1]=d_sort[i+1],d_sort[i]
    for i in range(3):
        print(*d_sort[i])
