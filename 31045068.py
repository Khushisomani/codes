# cook your dish here
for _ in range(int(input())):
    x=[0]*9
    for i in range(int(input())):
        a,b=map(int,input().split())
        if a<9:
            if x[a]<b:
                x[a]=b
    print(sum(x))