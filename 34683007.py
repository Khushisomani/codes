# cook your dish here
n = int(input())
budgets = []
total = []

for _ in range(n):
    budgets.append(int(input()))
budgets.sort()
for i in range(n):
    A = budgets[i]*(n-i)
    total.append(A)
total.sort()
print(total[-1])    

