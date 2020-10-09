# cook your dish here
for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        input()
    count=n
    while n>=6:
        count+=(n//2)
        n//=2 
    print(count)
    