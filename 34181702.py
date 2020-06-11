for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    d={}
    s=[]
    c=0
    s.append(a[0])
    for i in a:
        d[i]=a.count(i)
    if len(b)==len(set(d.values())):
        for i in range(1,n):
            if a[i]==a[i-1]:
                pass
            else:
                if a[i] in s:
                    c=1 
                    break
                else:
                    s.append(a[i])
        if c==1:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
    