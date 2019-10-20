# cook your dish here
for _ in range(int(input())):
    o=input()
    l=list(o.split())
    p=""
    for r in range(len(l)):
        j=l[r]
        if(r==len(l)-1):
            s=j[0]
            m=s.upper()
            q=j[1:]
            q=q.lower()
            m=m+q
            if(r>0):
                p=p+" "+m
            else:
                p=p+m

        else:
            s=j[0]
            m=s.upper()
            q='.'
            m=m+q
            p=p+" "+m
    print(p)

