# cook your dish here
# cook your dish here
# cook your dish here

def binary_search(interval, x):
    start,end=0,len(interval)-1 
    while start<=end:
        mid=(start+end)//2 
        if interval[mid][0]<=x<interval[mid][1]:
            return mid 
        elif interval[mid][0]>x:
            end=mid-1 
        else:
            start=mid+1 
    return [start,mid]
  

t = int(input())
while t>0:
    n, m = map(int, input().split())
    interval = []
    for i in range(n):
        l, r = map(int, input().split())
        interval.append([l, r])
    p = []
    for i in range(m):
        p.append(int(input()))
    
    interval = sorted(interval, key=lambda x: x[0])
    
    for x in p:
        wait_time = binary_search(interval, x)
        if isinstance(wait_time,list):
            l,r=wait_time
            if l>=n:
                print(-1)
            else:
                print(interval[l][0]-x)
        else:
            print(0)
                
       
    
    t-=1