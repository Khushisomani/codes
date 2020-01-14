# cook your dish here
for _ in range(int(input())):
    rank=0
    a=input().split()
    for i in range(int(a[0])):
        b=input().split()
        if b[0]=="CONTEST_WON":
            if int(b[1])<21:
                rank=rank+300+20-int(b[1])
            else:
                rank=rank+300
        if b[0]=="TOP_CONTRIBUTOR":
            rank=rank+300
        if  b[0]=="BUG_FOUND":
            rank=rank+int(b[1])
        if b[0]=="CONTEST_HOSTED":
            rank=rank+50 
    if a[1]=="INDIAN":
        print(rank//200)
    else:
        print(rank//400)
                