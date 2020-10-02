# cook your dish here
for _ in range(int(input())):
    l,d,s,c=map(int,input().split())
    for i in range(d-1):
        if s>=l:
            break
        s=s+c*s
    if s>=l:
        print('ALIVE AND KICKING')
    else:
        print('DEAD AND ROTTING')
        