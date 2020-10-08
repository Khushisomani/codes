import numpy as np;
n,k = map(int,input().split())
head = np.zeros(n,bool)
while(k):
	o,a,b = map(int ,input().split())
	if o == 0 :
		head[a:b+1] = ~head[a:b+1]
	else :
		print(str(np.count_nonzero(head[a:b+1])))
	k-=1		
