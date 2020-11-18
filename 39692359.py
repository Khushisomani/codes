# cook your dish here
t=int(input())
import math
while(t>0):
    n=int(input())
    c=0
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            c+=i
            if n//i!=i:
                c+=n//i
    print(c)
    t-=1