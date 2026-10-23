class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid) #rows
        n=len(grid[0]) #columns
        mins=[[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    mins[i][j]=grid[i][j]
                elif i==0 and j>0:
                    mins[i][j]=grid[i][j]+mins[i][j-1]
                elif i>0 and j==0:
                    mins[i][j]=grid[i][j]+mins[i-1][j]
                else:
                    mins[i][j]=grid[i][j]+min(mins[i-1][j],mins[i][j-1])
        return mins[m-1][n-1]

        