# cook your dish here
n,k=map(int,input().split())
l=list(map(int,input().split()))
if k==0:
    for i in l:
        print(i,end=" ")
else:
    if k%2==0:
        s=max(l)
        for i in range(len(l)):
            l[i]=s-l[i]
    s=max(l)
    for i in l:
        print(s-i,end=' ')
        