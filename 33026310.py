# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=1 
    a=[]
    for i in range(len(l)-1):
        if (l[i+1]-l[i])<=2:
            c+=1 
        else:
            a.append(c)
            c=1 
    a.append(c)
    print(min(a),max(a))
        
        