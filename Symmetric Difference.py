# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
l=set(map(int,input().split()))
n=int(input())
p=set(map(int,input().split()))
a=l.symmetric_difference(p)
a=list(a)
a.sort()
for i in a:
    print(i)
