# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    a=bin(a).count('1')
    b=bin(b).count('1')
    c=abs((a+b)-n)
    s=0
    for i in range(c,n):
        s+=2**i 
    print(s)