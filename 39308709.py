# cook your dish here
def good(mid,n,candy,ballons,m):
    add=0 
    for i in range(n):
        now=ballons[i]-(mid//candy[i])
        add+=max(0,now)
        if add>m:
            return False
    return True
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
low=0
high=10^18
while low<=high:
    mid=low+(high-low)//2
    if good(mid,n,b,a,m):
        high=mid-1
    else:
        low=mid+1
print(low)
    