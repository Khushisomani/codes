# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    s=a*b-1
    if(s%2!=0):
        print("Yes")
    else:
        print("No")