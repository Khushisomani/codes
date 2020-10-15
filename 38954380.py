n,x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append((abs(a[i]-b[i]),i))
l.sort(reverse=True)
s=0
for p,i in l:
    c=max(a[i],b[i])
    if c==a[i] and x>0:
        s+=c
        x-=1
    elif c==b[i] and y>0:
        s+=c 
        y-=1 
    elif c==a[i] and x==0:
        s+=b[i] 
        y-=1 
    elif c==b[i] and y==0:
        s+=a[i]
        x-=1
print(s)