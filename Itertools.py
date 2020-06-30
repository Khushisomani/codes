from itertools import combinations
n=input()
l=input().split()
k=int(input())
c=list(combinations(l,k))
count=0
for i in c:
    if 'a' in i:
        count+=1 
print(count/len(c))