# cook your dish here
def prime(n):
    total=0
    i=2 
    while i*i<=n:
        while n%i==0:
            total+=1 
            n/=i
        i+=1 
    if i>1:
        total+=1 
    return total
for _ in range(int(input())):
    x,k=map(int,input().split())
    if (prime(x))>=k:
        print(1)
    else:
        print(0)
        