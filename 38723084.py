# cook your dish here
for _ in range(int(input())):
    a,b=input().split()
    n=int(input())
    c=a+b
    x=''
    for i in range(n):
        x+=input()
    count=0
    d={}
    y=set(c)
    for i in y:
        d[i]=c.count(i)
    for i in x:
        if i in d and d[i]!=0:
            d[i]-=1 
        else:
            count=1 
            break 
    if count==1:
        print('NO')
    else:
        print('YES')
            
        
    