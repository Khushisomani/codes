# cook your dish here
for _ in range(int(input())):
    l=list(map(int,input().split()))
    a=[]
    for i in range(l[0]):
       a.append(list(map(int,input().split())))
    s=t=0
    for i in range(l[0]):
        if a[i][0]==1:
            if a[i][1]>=l[1] or a[i][1]>=l[1]-l[2]:
                s+=1
            elif l[4]>1:
                l[4]-=1 
                s+=1
            else:
                t= 1 
                print(s)
                break
        else:
            if a[i][1]<=l[3]:
                s+=1 
            elif l[4]>1:
                l[4]-=1
                s+=1
            else:
                t=1 
                print(s)
                break
    if t==0:
        print(s)