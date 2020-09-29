from collections import defaultdict
l,r=['d','f'],['j','k']
for _ in range(int(input())):
    n=int(input())
    d=defaultdict(int)
    time=0
    for i in range(n):
        s=input()
        count=2
        if s not in d:
            for j in range(1,len(s)):
                if s[j] in r and s[j-1] in r:
                    count+=4 
                elif s[j] in l and s[j-1] in l:
                    count+=4 
                else:
                    count+=2 
            d[s]=count
            time+=count
            
        else:
            time+=d[s]//2 
    print(time)
                
            
    