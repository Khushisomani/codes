# cook your dish here
for _ in range(int(input())):
    s=input()
    a=0
    for i in range(len(s)):
        if ord('a')<=ord(s[i])<=ord('z'):
            continue
        else:
            a+=int(s[i])
    print(a)
        