# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    dish={}
    p_s=0
    for i in s:
        dish[i]=0 
    for i in l:
        if p_s!=i:
            dish[i]+=1 
            p_s=i 
        else:
            p_s=0
    g_d=0 
    g_d_t=0
    for i in dish:
        if dish[i]>g_d:
            g_d=dish[i]
            g_d_t=i 
        elif dish[i]==g_d:
            if i<g_d_t:
                g_d_t=i 
    print(g_d_t)
            