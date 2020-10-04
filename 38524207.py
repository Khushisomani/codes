# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    cost=0
    i=0
    while i<len(l):
        if i%4==0 or i%4==1:
            cost+=l[i]
        i+=1
    print(cost)
            