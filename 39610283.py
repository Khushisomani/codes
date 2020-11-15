import math
x,n=map(int,input().split())
ans=0
for j in range(n):
    a=input()
    l=53
    for i in range(0,33,4):
        s=(a[i],a[i+1],a[i+2],a[i+3],a[l],a[l-1]).count('0')
        l-=2
        if s>=x:
            ans+=(math.factorial(s)/(math.factorial(x)*math.factorial(s-x)))
print(int(ans))
        