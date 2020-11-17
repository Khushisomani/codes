for _ in range(int(input())):
    n, k = [int(j) for j in input().split()]
    nums = [int(j) for j in input().split()]
    modulo = [0 for _ in range(k+1)]
    solved = False
    for num in nums:
      modulo[num % (k+1)] += 1
    for mod in modulo:
      solved = solved or mod >= n-1
    if solved:
      print("YES")
    else:
      print("NO")