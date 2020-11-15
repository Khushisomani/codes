# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    count=0
    for i in s:
        if i<=n:
            count+=1 
    print(n-count)