for _ in range(int(input())):
    s=input()
    pl=0
    vl=0
    oc=0
    for i in range(len(s)):
        if s[i]=="<":
            oc+=1 
        else:
            oc-=1 
        if oc<0:
            break 
        pl+=1 
        if oc==0:
            vl=pl 
    print(vl)