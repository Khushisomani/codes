# cook your dish here
for _ in range(int(input())):
    n=input()
    l=list(map(int,input().split()))
    l.sort()
    count=0
    s=0
    for i in range(len(l)):
        if l[i]<=s:
            s+=1 
            count+=1 
        else:
            break
    print(count)