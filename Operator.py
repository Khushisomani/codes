#!/bin/python3

import math
import os
import random
import re
import sys
import math
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    a=(meal_cost*tip_percent)/100
    b=(meal_cost*tax_percent)/100
    if (a+b+meal_cost)%1>0.5:
        print(math.ceil(a+b+meal_cost))
    else:
        print(math.floor(a+b+meal_cost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
