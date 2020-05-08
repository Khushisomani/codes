# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=[]
    
    for i in range(len(l)):
        if l[i]%2==0:
            for j in range(i+1,len(l)):
                s=[]
                if l[j]%2==1:
                    s.append(i)
                    s.append(j) 
                if len(s)>0:
                    k.append(s) 
    print(len(k))
    