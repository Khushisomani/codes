# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    d=0
    while a!=b:
        d+=1 
        if a>b:
            a=a//2 
        else:
            b=b//2 
    print(d)