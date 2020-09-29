# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    count=0
    if n==1:
        if s[0]=='0':
            print(1)
            continue
    else:
        for i in range(n):
            if i==0:
                if s[0]=='0' and s[1]=='0':
                    count+=1 
            elif i==n-1:
                if s[i]=='0' and s[i-1]=='0':
                    count+=1 
            else:
                if s[i]=='0':
                    if s[i-1]=='0' and s[i+1]=='0':
                        count+=1 
    print(count)
                
                
            