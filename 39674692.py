# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    c.sort(reverse=True)
    b1=0 
    b2=0
    for i in range(len(c)):
        if b1<b2:
            b1+=c[i]
        else:
            b2+=c[i]
    print(max(b1,b2))
        
        