# cook your dish here
import sys
n = int(input())
s=[]
for i in range(n):
    s.append(int(input()))
large_values = []
value = 0
for num in s:
    if num > value:
        for m in large_values:
            if m & num > value:
                value = m & num
        large_values.append(num)
print(value)