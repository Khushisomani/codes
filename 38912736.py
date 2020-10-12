# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    vis=[0]*n 
    res=[]
    for i in range(m):
        a,b=map(int,input().split())
        l.append([a,b])
    for i in range(m-1,-1,-1):
        a=l[i][0]
        b=l[i][1]
        if vis[a]==0 and vis[b]==0:
            vis[a]=1 
            vis[b]=1 
            res.append(i)
    print(*(reversed(res)))
        
        