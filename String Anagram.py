#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    main_count = 0
    total = 0
    string1_set = set(a + b)
    for i in range(len(string1_set)):
            count = a.count(list(string1_set)[i])
            count2 = b.count(list(string1_set)[i])
            print(count,count2)
            if count > count2: 
                main_count = count - count2
            elif count2 > count :
                main_count = count2 - count
            elif count2 == count :
                main_count = 0
            total = total + main_count
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
