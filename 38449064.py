from itertools import combinations
for _ in range(int(input())):
    n,m = map(int,input().split())
    arr=[]
    flag=1
    for i in range(n):
        arr.append(int(input()))
    if m in arr:
        print('Yes')
    elif sum(arr)==m:
        print('Yes')
    elif sum(arr)<m:
        print("No")
    else:
        for i in range(1,len(arr)+1):
            l=list(combinations(arr,i))
            flag=0
            for j in combinations(arr,i):
                if sum(j)==m:
                    print('Yes')
                    flag=1
                    break 
            if flag==1:
                break 
        if flag==0:
            print('No')
            