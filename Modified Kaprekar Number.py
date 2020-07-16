p=int(input())
q=int(input())
count=0
for i in range(p,q+1):
    b=len(str(i))
    s=i**2
    a=str(s)
    x=a[len(a)-b:]
    y=a[:len(a)-b]
    if len(y)>0:
        z=int(x)+int(y)
    else:
        z=int(x)
    if z==i:
        print(i,end=" ")
        count+=1
if count==0:
    print('INVALID RANGE')
