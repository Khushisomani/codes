for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for j in range(n):
        l.append([])
    for j in range(m):
        x,y=map(int,input().split())
        l[x-1].append(y-1)
        l[y-1].append(x-1)
    r=[a[i]/b[i] for i in range(n)]
    m=max(r)
    final=[]
    vis=[0]*n 
    for i in range(n):
        if r[i]==m:
            if vis[i]==0:
                vis[i]=1 
                q=[i]
                temp=[i+1]
                while len(q):
                    t=q.pop(0)
                    for j in l[t]:
                        if r[j]==m and vis[j]==0:
                            vis[j]=1 
                            q.append(j)
                            temp.append(j+1)
                if len(temp)>len(final):
                    final=temp.copy()
    print(len(final))
    for i in final:
        print(i,end=" ")
    print()
                    
                            