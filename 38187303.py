# cook your dish here
for _ in range(int(input())):
    d,u,n=map(float,input().split())
    s=d*u 
    count=0
    for i in range(int(n)):
        m,r,c=map(float,input().split())
        total=c/m+(r*u)
        if total<s:
            s=total
            count=i+1
    print(count)
    
        
    