# cook your dish here
n=int(input())
l=set(map(int,input().split()))
for i in range(1,n+1):
    if i not in l:
        print(i,end=" ")