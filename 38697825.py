for _ in range(int(input())):
    r,c = map(int, input().split())
    l=[]
    word = 'spoon'
    for i in range(r):
        l.append(list(input()))
    flag=0
    for i in range(r):
        temp=''.join(l[i])
        if word in temp.lower():
            flag=1
            break
        
    if flag==1:
        print("There is a spoon!")
    else:
        for j in range(c):
            temp=''
            for i in range(r):
                temp+=l[i][j]
            if word in temp.lower():
                flag=1 
                break
        if flag==1:
            print("There is a spoon!")
        else:
            print("There is indeed no spoon!")