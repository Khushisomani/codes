# cook your dish here
for _ in range(int(input())):
    k=int(input())
    l=list(map(int,input().split()))
    flag=True 
    s=1.0
    for i in range(k):
        if s<l[i]:
            flag=False 
            break 
        else:
            s=2*(s-l[i])
    if s==0 and flag==True:
        print('Yes')
    else:
        print('No')