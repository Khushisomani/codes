for _ in range(int(input())):
    s={}
    s1={}
    c=set({})
    for i in range(12):
        l=list(map(str,input().strip().split()))
        d=int(l[1])-int(l[3])
        b=-d
        if l[0] in s:
            s1[l[0]]+=d 
            if d>0:
                s[l[0]]+=3 
            elif d==0:
                s[l[0]]+=1 
        else:
            s1[l[0]]=d 
            if d>0:
                s[l[0]]=3 
            elif d==0:
                s[l[0]]=1 
            else:
                s[l[0]]=0
        if l[4] in s:
            s1[l[4]]+=b 
            if b>0:
                s[l[4]]+=3 
            elif b==0:
                s[l[4]]+=1 
        else:
            s1[l[4]]=b 
            if b>0:
                s[l[4]]=3 
            elif b==0:
                s[l[4]]=1 
            else:
                s[l[4]]=0
        c.add(l[0])
        c.add(l[4])
    c=list(c)
    d=max(s.values())
    a=-10000000000
    for i in c:
        if s[i]==d and a<s1[i]:
            f=i 
            a=s1[i] 
    s[f]=-10000000000
    a=-10000000000
    d=max(s.values())
    for i in c:
        if s[i]==d and a<s1[i]:
            k=i 
            a=s1[i]
    print(f,k,sep=' ')
    
   
            
            
        