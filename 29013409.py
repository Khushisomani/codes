# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append(l.count(l[i]))
    count=0
    for i in range(n):
        if l[i]==i+1:
            count=count+1 
    
    p=0
    for i in range(n):
        if a[i]==1:
            p=p+1
    s=0
            
    for i in range(n):
        if 0<l[i] and l[i]<n+1:
            continue
        else:
            s=1
            break
            
    if count!=n and p==n and s==0:
        print("yes")
    else:
        print("no")
        
            
    