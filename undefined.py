# cook your dish here
m=10**9+7
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    p=1 
    s=0 
    c=l[0]
    for i in range(1,n+1):
        s=(2*s+c*l[i]*2)%m
        c=(c+p*l[i])%m
        p=(2*p)%m 
    print(s)
    
    
        