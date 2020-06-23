# cook your dish here
for _ in range(int(input())):
    l=input()
    visited=[0]*len(l)
    count=0
    for i in range(len(l)-1):
        if l[i]=='x' and l[i+1]=='y' and visited[i]==0:
            count+=1 
            visited[i+1]=1 
        elif l[i]=='y' and l[i+1]=='x' and visited[i]==0:
            count+=1 
            visited[i+1]=1 
    print(count)