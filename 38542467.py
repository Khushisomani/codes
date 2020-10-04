# cook your dish here
for _ in range(int(input())):
    n,c,q=map(int,input().split())
    for i in range(q):
        a,b=map(int,input().split())
        if c>=a and c<=b:
            c=(a+b)-c 
    print(c)