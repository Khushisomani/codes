# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    count=0
    for i in range(len(l)):
        if (l[i]+k)>(s-l[i]):
            count+=1 
    print(count)