# cook your dish here
n,q=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in range(q):
    b=int(input())
    a.append(b) 
ma=max(l)
mi=min(l)
for i in range(len(a)): 
    if ma>=a[i] and mi<=a[i]:
        print("Yes") 
    else:
        print("No")
    
