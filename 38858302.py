# cook your dish here
def s(n):
    sum1=0
    if (n%10==n):
        return n 
    while n>0:
        sum1+=(n%10)
        n//=10 
    return sum1

n=int(input())
count=0
if n<11:
    for i in range(1,n):
        a=s(i)
        if i+a+s(i)==n:
            count+=1 
    print(count)
else:
    for i in range(1,100):
        a=n-i 
        if (n-i)<0:
            break
        b=s(n-i)
        if a+b+s(b)==n:
            count+=1 
    print(count)
