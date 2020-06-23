# cook your dish here
for _ in range(int(input())):
    t=int(input())
    if t%2==0:
        while(t%2==0):
            t=t//2 
        count=t//2
    else:
        count=t//2 
    print(count)