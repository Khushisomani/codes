# cook your dish here
for _ in range(int(input())):
    s=input()
    count0=s.count('s')
    count1=s.count('m')
    for i in range(len(s)):
        if (s[i]=="m") and (s[i-1]=="s" or s[i+1]=="s"):
            count0-=1 
            i=i+1
        
    if(count0==count1):
        print("tie")
    elif count0>count1:
        print("snakes")
    else:
        print("mongooses")