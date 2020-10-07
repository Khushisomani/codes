# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%2==0 or b%2==0:
        print('Tuzik')
    else:
        print('Vanka')