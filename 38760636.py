# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    min_p=[a[0]]*n 
    max_p=[a[0]]*n 
    for i in range(1,n):
        min_p[i]=min(min_p[i-1]+a[i],a[i])
        max_p[i]=max(max_p[i-1]+a[i],a[i])
    min_s=[a[-1]]*n
    max_s=[a[-1]]*n
    for i in range(n-2,-1,-1):
        min_s[i]=min(min_s[i+1]+a[i],a[i])
        max_s[i]=max(max_s[i+1]+a[i],a[i])
    ans=0
    for i in range(n-1):
        ans=max(ans,max_s[i+1]-min_p[i],max_p[i]-min_s[i+1])
    print(ans)
        
    
        