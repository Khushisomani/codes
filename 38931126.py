s=input()
d={}
a,b,c=0,0,0
d[(0,0,0)]=1
count=0
for i in range(len(s)):
    if s[i]=='A':
        a+=1
    if s[i]=='B':
        b+=1
    if s[i]=='C':
        c+=1
    mi=min(a,b,c)    
    if (a-mi,b-mi,c-mi) in d.keys():
        count+=d[(a-mi,b-mi,c-mi)]
        d[(a-mi,b-mi,c-mi)]+=1
    else:
        d[(a-mi,b-mi,c-mi)]=1
print(count)        