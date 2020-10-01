# cook your dish here
for _ in range(int(input())):
    n1,n2,m=map(int,input().split())
    c=m*(m+1)//2 
    if c>=n1 or  c>=n2:
        print(abs(n1-n2))
    else:
        print((n1+n2)-2*c)
        