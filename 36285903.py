# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%9==0:
        count1=a//9
    else:
        count1=a//9+1
    if b%9==0:
        count2=b//9
    else:
        count2=b//9+1
    if count1>=count2:
        print(1,count2)
    else:
        print(0,count1)
        
