# cook your dish here
for _ in range(int(input())):
    n=int(input())
    count=0
    for i in range(n):
        a,b=map(int,input().split())
        if b-a>5:
            count+=1 
    print(count)
            