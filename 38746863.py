# cook your dish here
for _ in range(int(input())):
    n=0
    for i in range(int(input())):
        a,b=map(int,input().split())
        n+=a-b 
    print(n)
        