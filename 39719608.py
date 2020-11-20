# cook your dish here
n = int(input())
a = input()
b = input()
lo,hi=0,n-1
res = '#'
while(lo <= hi):
    mid = (lo + hi)//2
    if(a[:mid+1] in b):
        res=a[:mid+1]
        lo=mid+1
    else:
        hi=mid-1
print(b.index(res))