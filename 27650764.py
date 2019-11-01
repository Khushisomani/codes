# cook your dish here
for _ in range(int(input())):
    p=input()
    s1=p.replace("U"," ")
    s2=p.replace("D"," ")
    count1=len(s1.split())
    count=len(s2.split())
    s=min(count,count1)
    print(s)
    