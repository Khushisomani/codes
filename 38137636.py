n=int(input())
l=list(map(int,input().split()))
l.insert(0,0)
visited=set()
ans=[]
for i in range(1,n+1):
    if i in visited:
        continue
    temp=[]
    j=i 
    while 1:
        temp.append(j)
        visited.add(j)
        j=l[j]
        if j==i:
            break 
    temp.append(i)
    ans.append(temp)
print(len(ans))
for i in ans:
    for j in i:
        print(j,end=" ")
    print()
    