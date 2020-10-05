# @Author: ASHISH SASMAL <ashish>
# @Date:   02-09-2020
# @Last modified by:   ashish
# @Last modified time: 17-09-2020

for _ in range(int(input())):
	k = int(input())
	a = 103993
	b = 33102
	m = a%b
	ans=""
	n=k
	while n>0:
	    p=0 
	    m=m*10 
	    while m<b:
	        p+=1 
	        m=m*10 
	        n-=1
	    ans+=("0"*p+str(m//b))
	    m=m%b 
	    n-=1 
	if k==0:
	    print(3)
	else:
	    print("3."+ans[:k])