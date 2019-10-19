# cook your dish here
for _ in range(int(input())):
    n,p=map(int,input().split())
    l=list(map(int,input().split()))
    k=p//2 
    s=p//10
    count=0
    for i in l:
        if i>=k:
            count=count+1
    if count==1:
        for i in l:
            if i<=s:
                count=count+1
            
    if count==3:
        print("yes")
    else:
        print("no")
          
      