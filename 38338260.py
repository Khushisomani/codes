# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=0
    for i in range(n):
        a=max(a,l[i]+i)
    print(a)