# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        k=int(input())
        l.append(k)
        
    s=[]
    su=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            p=l[i]*l[j]
            s.append(p)
    for i in range(len(s)):
        a=s[i]
        sum=0
        while(a!=0):
            b=a%10
            sum=sum+b
            a=a//10
        su.append(sum)
    max=0
    for i in range(len(su)):
        if(max<su[i]):
            max=su[i]
    print(max)

    
        