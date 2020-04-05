# cook your dish here
for _ in range(int(input())):
    cost=0
    for i in range(int(input())):
        a,b,c=map(int,input().split())
        x=a 
        x+=(c*x)/100
        x-=(c*x)/100
        l=(a-x)*b 
        cost+=l
    print(cost)