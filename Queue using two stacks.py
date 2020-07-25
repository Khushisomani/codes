q=int(input())
queue=[]
for i in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        queue.append(a[1])
    elif a[0]==2:
        queue.pop(0)
    else:
        print(queue[0])