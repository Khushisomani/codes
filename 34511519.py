# cook your dish here
for _ in range(int(input())):
    s=input()
    i=0
    count=0
    while i<len(s)-1: 
        if s[i]=='x' and s[i+1]=='y':
            count+=1 
            i+=2
        elif s[i]=='y' and s[i+1]=='x':
            count+=1 
            i+=2 
        else:
            i+=1
    print(count)
            