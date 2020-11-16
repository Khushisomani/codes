
def knap(t,w,n):

    s = [ [0 for i in range(w+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                s[i][j]=0
            else:
                if t[i-1]<=j:
                    s[i][j]=max(s[i-1][j],s[i-1][j-t[i-1]]+p[i-1]*c[i-1])
                else:
                    s[i][j]=s[i-1][j]
    return s[n][w]




for k in range(int(input())):
    n,w= map(int,input().split())

    c,p,t=[],[],[]


    for j in range(n):
        a,b,y = map(int,input().split())
        c.append(a)
        p.append(b)
        t.append(y)
        

    u=(knap(t,w,n))

    print(u)

        
