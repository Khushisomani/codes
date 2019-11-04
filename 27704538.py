# cook your dish here
import math
a=int(input())
b=int(input())
c=int(input())
root=(-b+math.sqrt(b**2-4*a*c))/(2*a)
root1=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print(root)
print(root1)