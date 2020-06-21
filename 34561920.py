# cook your dish here
for _ in range(int(input())):
    t,k=map(int,input().split())
    l=list(map(int,input().split()))
    count=0
    count1=0
    for i in range(len(l)):
        if l[i]>k:
            count+=k 
            count1+=l[i]
        else:
            count+=l[i] 
            count1+=l[i]
    print(count1-count)