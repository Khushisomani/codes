# cook your dish here
for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    l=0
    for i in range(n-1):
        if (x)%n==y:
            l=1 
            break 
        x=(x+k)
    if l==1:
        print('YES')
    else:
        print('NO')