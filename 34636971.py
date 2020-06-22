# cook your dish here
for _ in range(int(input())):
    n,b,m=map(int,input().split())
    l=list(map(int,input().split()))
    count=1
    for i in range(1,m):
        if l[i]//b!=l[i-1]//b:
            count+=1 
    print(count)