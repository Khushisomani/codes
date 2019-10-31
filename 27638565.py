# cook your dish here
for _ in range(int(input())):
    n,b=map(int,input().split())
    l=[]
    for i in range(n):
        w,h,p=map(int,input().split())
        if(p<=b):
            l.append(w*h) 
    if len(l)>0:
        print(max(l))
    else:
        print("no tablet")