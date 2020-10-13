# cook your dish here
for _ in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    flag=True 
    for i in range(n,0,-1):
        if i%b[i-1]!=0:
            flag=False
            print('NO')
            break 
    if flag==True:
        print('YES')
            