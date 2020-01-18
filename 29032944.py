# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    a=[]
    for i in range(n):
        s=l[i]*20-m[i]*10
        if s<0:
            s=0
        a.append(s)
    print(max(a))