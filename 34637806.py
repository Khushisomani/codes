# cook your dish here
for _ in range(int(input())):
    l,r=map(int,input().split())
    count=0
    for i in range(l,r):
        if (i==2 or i==8 or i==14 or i==20):
            count+=1
        else:
            count+=2 
    if (r==3 or r==9 or r==15 or r==21):
        count+=1
    print(count)
    