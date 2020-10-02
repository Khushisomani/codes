# cook your dish here
n=int(input())
l=list(map(int,input().split()))
q=int(input())
l.sort()
for i in range(1,n):
    l[i]+=l[i-1]
for i in range(q):
    k=int(input())
    a=n//(k+1)
    if n%(k+1)!=0:
        a+=1 
    a-=1 
    print(l[a])
    