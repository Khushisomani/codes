# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=n**0.5
    if s==int(s):
        print(0)
    else:
        mi=n
        for i in range(1,int(s)+1):
            if n%i==0:
                if abs((n/i)-i)<mi:
                    mi=abs((n/i)-i)
        print(int(mi))
            
            
    
    