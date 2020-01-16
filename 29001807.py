# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    c=0
    for i in range(len(l)):
        if l[i]==0:
            break
        else:
            c=c+1
    for i in range(c,len(l)):
        if l[i]==1: 
            count=count+100
        else:
            count=count+1100
    print(count)