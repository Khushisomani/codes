# cook your dish here
for _ in range(int(input())):
    sum1=0
    c=list(map(int,input().split()))
    a=list(input())
    s=list(set(a))
    if len(s)==26:
        print(0)
    else:
        for i in range(97,123):
            if chr(i) not in a:
                sum1=sum1+c[i%97]
        print(sum1)        
