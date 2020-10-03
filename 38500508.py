import string
n,s=map(str,input().split())
n=int(n)
d={i:[] for i in list(string.ascii_lowercase)}
for i in range(26):
    d[chr(97+i)]=s[i]
for i in range(n):
    p=input()
    a=''
    for i in p:
        if i=='_':
            a+=" "
        elif i in '.,!?':
            a+=i
        elif i.isupper():
            k=i.lower()
            a+=d[k].upper()
        else:
            a+=d[i]
    print(a)
            
    