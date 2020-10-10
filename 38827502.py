mi=10000000
ma=0
mni=0 
mai=0
for i in range(int(input())):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=((x1-x2)**2+(y1-y2)**2)**0.5
    b=((x3-x2)**2+(y3-y2)**2)**0.5
    c=((x1-x3)**2+(y1-y3)**2)**0.5
    s=(a+b+c)/2 
    s=(s*(s-a)*(s-b)*(s-c))**0.5 
    if s<=mi:
        mi=s 
        mni=i+1
    if s>=ma:
        ma=s
        mai=i+1
print(mni,mai,end=" ")