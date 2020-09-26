# cook your dish here
for _ in range(int(input())):
    s=input()
    a=set()
    i=0
    while i<len(s)-1:
        p=s[i]+s[i+1]
        a.add(p)
        i+=1 
    print(len(a))