# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    x=["a","e","i","o","u"]
    count=0
    for i in range(len(s)-1):
        if s[i] not in x and s[i+1] in x:
            count=count+1 
    print(count)
            