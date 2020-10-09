# cook your dish here
d = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
for _ in range(int(input())):
    a=input()
    try:
        if len(a)==5 and a[0] in d and a[1] in '12345678' and a[2]=='-' and a[3] in d and a[4] in '12345678':
                y=[-2,-2,2,2,-1,1,-1,1]
                x=[1,-1,1,-1,2,2,-2,-2]
                i=int(a[1])
                j=d[a[0]]
                p=int(a[4])
                q=d[a[3]]
                for k in range(len(x)):
                    if i+x[k]==p and j+y[k]==q:
                        print('Yes')
                        break 
                else:
                    print('No')
        else:
            print('Error')
    except:
        print('Error')