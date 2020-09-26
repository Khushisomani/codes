# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=2
    count=0
    for i in range(1,len(l)-1):
        if l[i]!=l[i-1] or l[i]!=l[i+1]:
            count+=1 
    if l[0]!=l[1]:
        count+=1 
    if l[-1]!=l[-2]:
        count+=1
    print(count)
            
    