# cook your dish here
for _ in range(int(input())):
    s=input()
    l_s=s[1:]+s[0]
    r_s=s[len(s)-1]+s[:len(s)-1]
    if l_s==r_s:
        print('YES')
    else:
        print('NO')