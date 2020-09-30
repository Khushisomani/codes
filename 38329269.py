import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = a[0]
    for i in range (1, n):
        x = math.gcd(a[i], x)
        
    if x == 1:
        print(n)
    else:
        print(-1)