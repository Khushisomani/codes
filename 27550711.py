# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(input().split())
    count=0
    for i in range(len(l)):
        if l[len(l)-1]!="cookie":
            if l[i]=="cookie" and l[i+1]=="milk" or l[i]=="milk":
                count=1 
        else:
            count=0 
            break
    if count==1:
        print("YES")
    else:
        print("NO")