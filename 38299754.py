# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    count=0
    s=abs(a-b)
    if int(s**0.5)==(s**0.5):
        count-=1 
    for i in range(1,int(s**0.5)+1):
        if s%i==0:
            count+=2 
    print(count)