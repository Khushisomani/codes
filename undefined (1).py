# cook your dish here
# cook your dish here
for _ in range(int(input())):
    p1=0
    p2=0
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    a.reverse()
    for i in range(n):
        if i==0:
            p1+=a[i]
        elif i==1 or i==2:
            p2=p2+a[i]
        elif i%2!=0:
            p1=p1+a[i]
        else:
            p2=p2+a[i]
    if p1>p2:
        print("first")
    elif p1<p2:
        print("second")
    else:
        print("draw")
