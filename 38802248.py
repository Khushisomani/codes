for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    flag=0
    s=0
    for i in range(n):
        s+=l[i]
        if l[i]<0:
            flag=1 
    if flag==0:
        print(s*k)
        continue 
    x=[]
    for i in range(2):
        x.extend(l)
    if k==1:
        a=l[0]
        b=l[0]
        for i in range(1,n):
            a=max(a+l[i],l[i])
            b=max(a,b)
        print(b)
    elif s>0:
        a=x[0]
        b=x[0]
        for i in range(1,2*n):
            a=max(a+x[i],x[i])
            b=max(a,b)
        print(b+(k-2)*s)
    else:
        a=x[0]
        b=x[0]
        for i in range(1,2*n):
            a=max(a+x[i],x[i])
            b=max(a,b)
        print(b)
        
        
        