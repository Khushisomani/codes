# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    l=[0,0]
    for i in s:
        if i=='0':
            l[0]+=1 
        else:
            l[1]+=1
    a=n//k
    o=l[0]//a
    e=l[1]//a
    if l[0]%a==0 and l[1]%a==0:
        temp="0"*o+"1"*e
        ans=""
        for i in range(a):
            if(i%2==0):
                ans=ans+temp
            else:
                ans=ans+temp[::-1]
        print(ans)
    else:
        print('IMPOSSIBLE')