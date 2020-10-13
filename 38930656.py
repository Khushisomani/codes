# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    d={}
    for i in range(n):
        a,v=map(int,input().split())
        if a not in d:
            d[a]=v 
        else:
            d[a]=max(d[a],v)
    l=sorted(d.values())
    print(l[-1]+l[-2])