# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    diff=[]
    for i in range(len(l)-1):
        a=abs(l[i+1]-l[i])
        diff.append(a)
    print(min(diff))

            