n,m=list(map(int, input().split()))
l=list(map(int, input().split()))
a=set(map(int, input().split()))
b=set(map(int, input().split()))
h=0
for i in range(len(l)):
    if l[i] in a:
        h+=1
    elif l[i] in b:
        h-=1 
print(h)

