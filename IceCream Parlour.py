#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    costs=Counter(cost)
    half=money/2
    combo=set()
    for i in costs:
        if(i!=half and money-i in costs) or (i==half and costs[i]>1):
            combo.add(i)
    for index,i in enumerate(cost,1):
        if i in combo:
            print(index,end=" ")
    print()
            


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
