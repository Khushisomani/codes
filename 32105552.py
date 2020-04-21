# cook your dish here
for _ in range(int(input())):
    n,q=map(int,input().split())
    s=0
    cost=0
    for i in range(q):
        a,b=map(int,input().split())
        cost+=abs(s-a)
        cost+=abs(a-b)
        s=b 
    print(cost)
            