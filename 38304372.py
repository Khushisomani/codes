for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l[0]
    result=0
    for i in l:
        if i>a:
            result=max(result,i-a)
        else:
            a=i 
    if result==0:
        print('UNFIT')
    else:
        print(result)