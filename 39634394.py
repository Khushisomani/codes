# cook your dish here
for u in range(int(input())):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    l=[]
    c=[0]*n
    s=0
    for i in d:
        c[i]+=1
    for i in range(n):
        f=list(map(int,input().split()))
        x=f[0]
        f=f[1:]
        f.sort(reverse=True)
        l.append([x]+f)
    for i in range(n):
        if(c[i]>0):
            if(c[i]<=l[i][0]):
                s+=sum(l[i][1:c[i]+1])
            else:
                s+=sum(l[i][1:])
    print(s)