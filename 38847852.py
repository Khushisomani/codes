# cook your dish here
for _ in range(int(input())):
    a='abcdefghijklmnopqrstuvwxyz'
    n=int(input())
    if n<26:
        print(a[:n])
    else:
        s=''
        s=a 
        b=n 
        b-=26
        while b>=26:
            s+=a 
            b-=26 
        s+=a[:b]
        print(s)