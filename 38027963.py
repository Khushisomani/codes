# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    l=map(int,input().split())
    l=set(l)
    if 0 in l:
        l.remove(0)
    print(len(l))
    t-=1    
    
    