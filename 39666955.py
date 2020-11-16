# cook your dish here
from collections import deque
def use_q(l,q,mx):
    l_1=deque(sorted(l,reverse=True))
    l_2=deque()
    for i in range(1,mx+1):
        if not l_2 or l_1[0]>l_2[0]:
            t_2=l_1.popleft()
            if i in q:
                print(t_2)
            t_2=t_2//2
            if t_2>0:
                l_2.append(t_2)
        else:
            t_3=l_2.popleft()
            if i in q:
                print(t_3)
            t_3=t_3//2
            if t_3>0:
                l_2.append(t_3)
        if not l_1:
            l_1,l_2=l_2,l_1
            
n,m=map(int,input().split())
l=list(map(int,input().split()))
q=set([])
m_1=-1
for i in range(m):
    t_4=int(input())
    q.add(t_4)
    m_1=max(m_1,t_4)
    
use_q(l,q,m_1)
    