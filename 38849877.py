# cook your dish here
for _ in range(int(input())):
    a=input().split(':')
    b=input().split(':')
    c=int(input())
    x=int(a[0])*60+int(a[1])
    y=int(b[0])*60+int(b[1])
    if y+2*c<x:
        print("{:.1f} {:.1f}".format(x-y+c,x-y))
    elif y+2*c==x:
        print("{:.1f} {:.1f}".format(x-y+c,x-y))
    else:
        a=c+((x-y)/2)
        print("{:.1f} {:.1f}".format(x-y+c,a))