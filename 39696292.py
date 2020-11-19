# cook your dish here
for _ in range(int(input())):
	x=int(input())
	l=[1,3]
	for i in range(3,x):
	    p=(i*(i+1))//2
	    l.append(p)
	    if p>x:
	        break
	print(min(len(l)+l[-1]-x,len(l)-1+x-l[-2]))
	
	        