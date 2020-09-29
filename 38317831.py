# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    count=0
    for i in range(1,n):
        if abs(l[i]-l[i-1])>1:
            count=1 
            break 
    if count==1:
        print('NO')
    else:
        print('YES')
