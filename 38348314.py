# cook your dish here
k,n=map(int,input().split())
l=[]
for i in range(k):
    l.append(input())
a=[]
for i in range(n):
    a.append(input())
for i in range(n):
    flg=0
    for j in range(k):
        if (l[j] in a[i]) or(len(a[i])>=47):
            print('Good')
            flg=1 
            break 
    if flg==0:
        print('Bad')
    
    