s=input()
t=input()
k=int(input())
l=0
for i in range(min(len(s),len(t))):
    if(s[i]==t[i]):
        l+=1  
    else:
        break 
a=(len(s)+len(t)-2*l)%2
b=k%2
if(len(s)+len(t)-2*l>k):
    print("No") 
elif a==b:
    print("Yes") 
elif (len(s)+len(t)-k<0):
    print("Yes")
else:
    print("No")



