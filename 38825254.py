# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=input().split()
    flag=0
    s=''.join(l).split('1')
    l=[]
    for i in s:
        if len(i)==0:
            continue 
        else:
            l.append(i)
    l.sort(reverse=True,key=len)
    if len(l)==0:
        print('No')
    elif len(l)==1:
        if (len(l[0]))%2==0:
            print('No')
        else:
            print('Yes')
    else:
        c,v=len(l[0]),len(l[1])
        if c%2==0:
            print('No')
        else:
            if c%2 and (c+1)/2>v:
                print('Yes')
            else:
                print('No')
        
        
            
            
        
                