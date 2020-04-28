for _ in range(int(input())):
    n=int(input())
    l0={}
    l1={}
    for i in range(n):
        w,s=input().split()
        s=int(s)
        if s==0:
            if w in l0:
                l0[w]+=1 
            else:
                l0[w]=1 
        else:
            if w in l1:
                l1[w]+=1 
            else:
                l1[w]=1
        
    ans=0 
    for x in l0:
        if x in l1:
            ans=ans+max(l0[x],l1[x]) 
            del l1[x] 
        else:
            ans+=l0[x]
    for x in l1:
        ans=ans+l1[x]
        
    print(ans)