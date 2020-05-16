# cook your dish here
for _ in range(int(input())):
    n,a,b,c,d,p,q,y= [int(num) for num in input().split()]
    city=list(map(int,input().split()))
    if (abs(city[c-1]-city[a-1])*p)>y:
        print(abs(city[b-1]-city[a-1])*p)
    else:
        print(min(p * abs(city[b - 1] - city[a- 1]), y + q * abs(city[d - 1] - city[c - 1]) + p * abs(city[b - 1] - city[d - 1])))
