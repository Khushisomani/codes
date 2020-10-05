for _ in range (int(input())):
    n = int(input())
    grid = []
    for i in range (n):
        grid.append(list(input()))
    grid.append(['.']*n)
    grid.reverse()
    count = 0
    for i in range(1,n+1):
        temp=0
        for j in range(n-1,-1,-1):
            if grid[i][j]=='.' and grid[i-1][j]=='.' and temp==0:
                count+=1 
            elif grid[i][j]=='.' and grid[i-1][j]=='#':
                grid[i][j]='#'
            else:
                temp=1 
    print(count)