# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    count=0
    count1=0
    s=0
    for i in range(n):
        if l[i]<=m[i]:
            s=s+1 
    if s==n:
        count+=1 
    s=0
    for i in range(n):
        if l[n-i-1]<=m[i]:
            s=s+1 
    if s==n:
        count1=count1+1 
    
    if count==1 and count1==1:
        print("both")
    elif count==1:
        print("front")
    elif count1==1:
        print("back")
    else:
        print("none")
            
            
        