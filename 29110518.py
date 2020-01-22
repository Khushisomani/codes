# cook your dish here
for _ in range(int(input())):
    s=input().split()
    k=0
    for i in s:
        if i=="not":
            k=1 
            break 
    if k==1:
        print('Real Fancy')
    else:
        print('regularly fancy')
    