for _ in range(int(input())):
    s,t,d=map(int,input().split())
    print(max(0,d-t-s,s-t-d,t-d-s))
