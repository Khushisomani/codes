from collections import defaultdict
t=int(input())
for _ in range(t):
    n,k,l=map(int,input().split())
    if n>k*l or k==1:
        if n==1 and k==1:
            print(1,end=" ")
        else:
            print(-1,end=" ")
    else:
        x=1
        while(n!=0):
            if(x==k+1):
                x=1
            print(x,end=" ")
            x+=1
            n-=1
    print()