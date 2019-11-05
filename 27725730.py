# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    count0=0 
    count1=0 
    for i in range(len(s)):
        if "A"<=s[i]<="Z":
            count0+=1
        if "a"<=s[i]<="z":
            count1+=1 
    if count0<=k and count1<=k:
        print("both")
    if count0>k and count1>k:
        print("none") 
    if count0>k and count1<=k:
        print("brother")
    if count0<=k and count1>k:
        print("chef")
    