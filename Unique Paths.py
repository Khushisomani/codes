class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for i in range(m):
            s=[]
            for j in range(n):
                if i==m-1 or j==n-1:
                    s.append(1)
                else:
                    s.append(0)
            dp.append(s)
            
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]