# cook your dish here
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=defaultdict(lambda:0)
    for k in l:
        i=2
        while i*i<=k:
            while k%i==0:
                k//=i
                d[i]+=1 
            i+=1 
        if k>1:
            d[k]+=1 
    ans=1 
    for i in d:
        ans=ans*(d[i]+1)
    print(ans)
        
