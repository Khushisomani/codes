# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    n-=1 
    k-=1 
    if k>n-k:
        k=n-k 
    a=1
    for i in range(k):
        a*=(n-i) 
        a/=(i+1)
    print(int(a))
        
        
            