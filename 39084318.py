# cook your dish here
def good(red,mid,blue,green):
    return ((red-mid)+(blue-mid)+green>=mid)
for _ in range(int(input())):
    n,r,g,b=map(int,input().split())
    left=0
    right=min(n,r,b)
    ans=0
    while left<=right:
        mid=(left+right)//2
        if good(r,mid,b,g):
            ans=mid
            left=mid+1 
        else:
            right=mid-1
    print(ans)
    
    