# cook your dish here
n=int(input())
l=list(map(int,input().split()))
s=n*(n+1)//2
k=sum(l)
if k!=s:
    print('NO')
else:
    print('YES')
