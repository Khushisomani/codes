for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    s=0
    i=0
    while i<len(l):
        s+=l[i]
        i+=2 
    print(s)
    