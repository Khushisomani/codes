# cook your dish here
for _ in range(int(input())):
    s=input()
    p=input()
    a=""
    for i in range(len(s)):
        if s[i]=="W" and p[i]=="W":
            a=a+"B" 
        elif s[i]=="B" and p[i]=="B":
            a=a+"W" 
        else:
            a=a+"B" 
    print(a)