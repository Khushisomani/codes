# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    l=l[::-1]
    cost=0
    k=0
    for i in range(0,len(l)):
        if int(l[i])>=k:
            cost=cost+l[i]-k
            k+=1
        else:
            break
    print(cost%1000000007)
            
            
        
    