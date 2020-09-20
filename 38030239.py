# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=[]
    for i in range(len(l)):
        if l[i] in s:
            continue 
        else:
            s.append(l[i])
    a=[]
    for i in s:
        a.append(l.count(i))
    s=set(a)
    p=[]
    for i in s:
        b=[]
        b.append(i)
        b.append(a.count(i))
        p.append(b)
    for i in range(len(p)):
        for j in range(len(p)-i-1):
            if p[j][1]<p[j+1][1]:
                p[j],p[j+1]=p[j+1],p[j]
    s=p[0][1]
    l=[]
    l.append(p[0][0])
    for i in range(1,len(p)):
        if p[i][1]==s:
            l.append(p[i][0])
    l.sort()
    print(l[0])
    
            
            
            
            
        
        
            
    
            
            
        
            
    