l=map(int,input().split())
i=0
j=0
k=0
while len(l)!=1:
    if j==1:
        j=0
        if i<len(l):
            if i!=len(l)-1:
                l.pop(i)
            else:
                l.pop(i)
                i=0
    else:
        j+=1
        if i==len(l)-1:
            i=0
        else:
            i+=1
            
print(l)               