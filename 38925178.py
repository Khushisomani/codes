# cook your dish here
for _ in range(int(input())):
    n,d=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    i=n-1 
    s=0
    while i>=1:
        if l[i]-l[i-1]<d:
            s+=l[i]+l[i-1]
            i-=2 
        else:
            i-=1 
    print(s)
        