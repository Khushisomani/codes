# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    x=9999999999
    l=list(map(int,input().split()))
    for i in range(len(l)):
        if b%l[i]==0:
            if x>b/l[i]:
                x=b/l[i]
                c=l[i]
    if x==9999999999:
        print(-1)
    else:
        print(c)