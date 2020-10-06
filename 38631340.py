# cook your dish here
while True:
    n=int(input())
    if n==0:
        break 
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    count=0
    for i in range(len(l)-2):
        first=l[i]
        left=i+1 
        right=len(l)-1 
        while left<right:
            if first>l[left]+l[right]:
                count+=(right-left)
                right-=1 
            else:
                left+=1 
    print(count)
    