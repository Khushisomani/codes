# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    s=max(l)
    p=max(m)
    sa=0
    sb=0
    for i in l:
        sa=sa+i 
    sa=sa-s
    for i in m:
        sb=sb+i 
    sb=sb-p
    if(sa<sb):
        print("Alice")
    elif(sa>sb):
        print("Bob")
    else:
        print("Draw")