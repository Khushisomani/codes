# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l[0]
    s=1
    for i in range(1,len(l)):
        if l[i]<a:
            a=l[i]
            s=(i+1)
    print(s)