# cook your dish here
for _ in range(int(input())):
    s=input()
    count=0
    
    for i in range(0,len(s)-1):
        if s[i]=="1" and s[i+1]=="0":
            count=count+1 
        if(s[i]=="0" and s[i+1]=="1"):
            count=count+1 
    if(s[len(s)-1]!=s[0]):
        count=count+1
    
    if count<=2:
        print("uniform")
    else:
        print("non-uniform")
            
            