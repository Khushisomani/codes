# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    while a>0 and b>0:
        a-=b 
        b=b//2
    if a<=0:
        print(1)
    else:
        print(0)