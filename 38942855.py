# cook your dish here
for _ in range(int(input())):
    r,s=input().split()
    a=set(r)
    b=set(s)
    x={}
    for i in a:
        x[i]=r.count(i)
    y={}
    for i in b:
        y[i]=s.count(i)
    c=True
    if a==b:
        for i in a:
            if x[i]!=y[i]:
                c=False
                break 
    if c==False:
        print('NO')
    else:
        print('YES')
    
        
        
        
    