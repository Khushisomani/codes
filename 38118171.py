# cook your dish here
n,d=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
count=0
i=1 
while i<n:
    if (l[i]-l[i-1])<=d:
        count+=1 
        i+=1 
    i+=1 
print(count)
        