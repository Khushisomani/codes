# cook your dish here
for _ in range(int(input())):
    s=list(input())
    a,b=map(int,input().split())
    c=s.index('B')-s.index('A')
    if(c%(a+b)==0):
        print("unsafe")
    else:
        print("safe")