# cook your dish here
for _ in range(int(input())):
    n=int(input())
    x=[[] for i in range(n)]
    for i in range(n-1):
        u,v=map(int,input().split())
        x[v-1].append(u-1)
    ans=-1 
    for i in x:
        if len(i)==0:
            ans+=1 
    print(ans)
        