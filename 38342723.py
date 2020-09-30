# cook your dish here
for _ in range(int(input())):
    n=int(input())
    i=0
    j=0
    while n%10==0:
        n=n//10 
        i+=1 
    while n%2==0:
        j+=1 
        n=n//2 
    if n==1 and i>=j:
        print('Yes')
    else:
        print('No')
        