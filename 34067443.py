import datetime
for i in range(int(input())):
    y,m,d=map(int,input().split(':'))
    oe=d%2
    count=1
    m=datetime.datetime(y,m,d)
    while True:
        m=m+datetime.timedelta(days=2)
        if m.day%2==oe:
            count+=1 
        else:
            break
    print(count)