# cook your dish here
for _ in range(int(input())):
    s=input()
    s1=''
    s2=''
    for i in range(len(s)):
        if i%2==0:
            s1+='+'
            s2+='-'
        else:
            s1+='-'
            s2+='+'
    count=0
    count1=0
    for i in range(len(s)):
        if s[i]!=s1[i]:
            count+=1 
        if s[i]!=s2[i]:
            count1+=1 
    print(min(count,count1))
            
    
            
                