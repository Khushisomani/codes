# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(int(input()))
    l.sort()
    s=(n+k)//2
    print(l[s])