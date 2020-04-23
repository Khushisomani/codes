# cook your dish here
for _ in range(int(input())):
    m,w=input().split()
    i=0
    j=0
    while(i<len(m) and j<len(w)):
        if(m[i]==w[j]):
            i+=1 
        j+=1
    k=0
    l=0
    while(k<len(w) and l<len(m)):
        if(w[k]==m[l]):
            k+=1 
        l+=1
    if(k==len(w) or i==len(m)):
        print('YES')
    else:
        print('NO')
            
    