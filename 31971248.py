# cook your dish here
from itertools import combinations
c=[]
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=list(combinations(a,k))
    s=[]
    for i in l:
        s.append(sum(i))
    b=s.count(min(s))
    c.append(b)
for i in c:
    print(i)
    
    