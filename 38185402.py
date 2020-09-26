# cook your dish here
for _ in range(int(input())):
    s=input()
    k,x=map(int,input().split())
    d={}
    c=0
    for i in s:
        if len(d)==0 or (i not in d):
            d[i]=1
            c+=1 
        elif d[i]<x:
            d[i]=d[i]+1 
            c+=1 
        elif(k>0):
            k-=1 
        else:
            break 
    print(c)
    