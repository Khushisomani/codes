# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    t=list(map(int,input().split()))
    p=list(map(int,input().split()))
    count=0
    for i in range(n):
        t[i]=k//t[i]
        if t[i]*p[i]>count:
            count=t[i]*p[i]
    print(count)