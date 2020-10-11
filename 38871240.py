for _ in range(int(input())):
    l,r,g=map(int,input().split())
    x=(l-1)//g 
    y=(r)//g 
    s=y-x 
    f=1
    if (s==1):
        if g<l or g>r:
            f=0 
    if f==1:
        print(s)
    else:
        print(0)