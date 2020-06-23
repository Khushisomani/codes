# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(2,n//2+1):
        if n%i==0:
            l.append(i)
    m=1
    for i in l:
        m*=i 
    if m>999:
        m=str(m)
        s=''
        s+=m[-4]
        s+=m[-3]
        s+=m[-2]
        s+=m[-1]
        print(s)
    else:
        print(m)