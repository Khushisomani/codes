# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a==b and c==d:
        print('YES')
    elif c==d and a!=b:
        print('NO')
    else:
        if (a-b)%(c-d)==0:
            print('YES')
        else:
            print('NO')