class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[]
        for i in range(n):
            s=[]
            for j in range(m):
                s.append(0)
            dp.append(s)
        dp[0][0]=grid[0][0]
        for i in range(1,n):
            dp[i][0]=grid[i][0]+dp[i-1][0]
        for i in range(1,m):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]