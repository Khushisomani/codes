# cook your dish he
n=int(input())
count=0
for _ in range(n):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=(x1-x2)**2+(y1-y2)**2
    b=(x2-x3)**2+(y2-y3)**2
    c=(x1-x3)**2+(y1-y3)**2
    l=[a,b,c]
    l.sort()
    if l[0]+l[1]==l[2]:
        count+=1 
print(count)
        
    
        
