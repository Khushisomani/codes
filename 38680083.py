# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    for i in range(n-1,-1,-1):
        if i==n-1:
            a=l[i].split()
            k=' '.join(a[2:])
            print('Begin on '+k)
        else:
            a=l[i].split()
            k=' '.join(a[2:])
            b=l[i+1].split()
            if b[0]=='Left':
                print('Right on '+k)
            else:
                print('Left on '+k)

        
        