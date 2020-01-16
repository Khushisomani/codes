# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[]
    l1=[]
    for i in range(n):
        s=input()
        s1=s.split()
        l.append(s)
        l1.append(s1[0])
    a=[]
    for i in range(n):
        a.append(l1.count(l1[i]))
    for i in range(n):
        if a[i]==1:
            print(l1[i])
        else:
            print(l[i])