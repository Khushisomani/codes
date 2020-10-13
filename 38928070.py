# cook your dish here
for _ in range(int(input())):
      n, k = map(int, input().split())
      lst = list(map(int, input().split()))
      
      y = 0
      for i in range(n):
            lst[i] = lst[i] + y
            if lst[i] < k:
                  print(i + 1)
                  break
            else:
                  y = lst[i] - k
                  
      if y > k:
            print((y // k) + n + 1)