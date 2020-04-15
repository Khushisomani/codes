# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=[]
    for i in range(len(l)):
        if l[i]==1:
            s.append(i+1)
    count=0
    for i in range(1,len(s)):
        if s[i]-s[i-1]<6:
            print('NO')
            break 
        else:
            count+=1 
    if count>=(len(s)-1):
        print("YES")