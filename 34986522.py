# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    m=0
    for i in range(n):
        a,b=map(int,input().split())
        a=str(a)
        x=0
        for i in range(len(a)):
            x+=int(a[i])
        y=0
        b=str(b)
        for i in range(len(b)):
            y+=int(b[i])
        if x>y:
            c+=1 
        elif y>x:
            m+=1 
        else:
            c+=1 
            m+=1 
    if c>m:
        print(0,c)
    elif m>c:
        print(1,m)
    else:
        print(2,c)
    
        
        