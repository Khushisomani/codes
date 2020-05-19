# cook your dish here

def l(lis,s):
    no=0
    index= 1
    for i in lis:
        no+=((i-index)//s)
        index=i+1
    return no


for _ in range(int(input())):
    n,m=map(int,input().split())
    X,Y,s=map(int,input().split())
    if X>0:
        x=list(map(int,input().split()))
    else:
        x=[]
    if Y>0:
        y=list(map(int,input().split()))
    else:
        y=[]
    x.append(n+1)
    y.append(m+1)
    a=l(x,s)
    b=l(y,s)
    print(a*b)