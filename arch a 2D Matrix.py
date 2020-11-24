class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        if n==0:
            return False
        m=len(matrix[0])
        if m==0:
            return False
        for i in range(n):
            if matrix[i][m-1]>=target:
                break
        t=False
        for j in range(m):
            if matrix[i][j]==target:
                t=True
                break
        return t
        
        