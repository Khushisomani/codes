t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    count1=0
    count2=0
    for i in range(n):
        if l[i]==0 or l[i]==1:
            count1+=1 
        if l[i]==2:
            count2+=1 
    
    temp1=n-count1 
    temp2=0
    if count2>=2:
        temp2=count2 
    print((temp1*(temp1-1)//2)-(temp2*(temp2-1)//2))
   
    