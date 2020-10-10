# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0 
    a=1
    for i in range(1,n):
        p=l[i-1]&l[i]
        if p!=l[i-1]:
            a=0
            break 
        else:
            c+=bin(p).count('1')
    if a==0:
        print(0)
    else:
        print((2**c)%(10**9+7))