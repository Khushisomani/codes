# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n=int(input())
shoe=collections.Counter(map(int,input().split()))
m=int(input())
cost=0
for i in range(m):
    a,b=map(int,input().split())
    if shoe[a]:
        cost+=b 
        shoe[a]-=1
print(cost)

