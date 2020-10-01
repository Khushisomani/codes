# cook your dish here
import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l[0]
    for i in range(1,len(l)):
        a=math.gcd(a,l[i])
    print(a)
    
    