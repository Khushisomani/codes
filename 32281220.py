# cook your dish here
for _ in range(int(input())):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    a=100
    b=100
    for i in range(n):
        if m[i]==0: 
            if l[i]<a:
                a=l[i]
        else:
            if l[i]<b:
                b=l[i]
    k=s+a+b
    if k<=100:
       print('yes')
    else:
        print('no')
    