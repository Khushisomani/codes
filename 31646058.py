# cook your dish here
n=int(input())
l=list(map(int,input().split()))
l=sorted(list(set(l)))
if len(l)==1:
    print(0)
else:
    print(l[-2])
    