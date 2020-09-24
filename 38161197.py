for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(list(input()))
    start=l[0]
    for i in range(1,len(l)):
        for j in range(len(start)):
            a=int(start[j])
            b=int(l[i][j])
            if a and b:
                start[j]=0
            elif a or b:
                start[j]=1 
    ans=0
    for i in start:
        if i==1:
            ans+=1 
    print(ans)