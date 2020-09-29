# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count1=0
    count2=0
    count=0
    for i in range(n):
        count1+=a[i]
        count2+=b[i]
        if count1==count2 and a[i]==b[i]:
            count+=a[i]
    print(count)