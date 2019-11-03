# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    sum2=0
    i=0
    while(i<n):
        sum2=sum2+l[i]
        if i+1<n:
            i=i+1
        else:
            break
        sum2=sum2+m[i]
        if i+1<n:
            i=i+1
        else:
            break
        
    
    sum1=0
    i=0
    while(i<n):
        sum1=sum1+m[i]
        if i+1<n:
            i=i+1
        else:
            break
        sum1=sum1+l[i]
        if i+1<n:
            i=i+1
        else:
            break
        
        
    if(sum2<sum1):
        print(sum2) 
    else:
        print(sum1)
        