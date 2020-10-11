import math
m=10**9+7
for _ in range(int(input())):
    a,b,n=map(int,input().split())
    if(abs(a-b)==0):
        print(pow(a,n,m)+pow(b,n,m)%m)
    else:
        d=pow(a,n,abs(a-b))+pow(a,n,abs(a-b))
        print(math.gcd(d,abs(a-b)))
    
    
    
    