class Solution:
    def closedIsland(self,grid:list[list[int]])->int:
        m=len(grid)
        n=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n:
                return False
            if grid[r][c]==1:
                return True
            grid[r][c]=1
            a=dfs(r+1,c)
            b=dfs(r-1,c)
            d=dfs(r,c+1)
            e=dfs(r,c-1)
            return a and b and d and e
        count=0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0 and dfs(i,j):
                    count+=1
        return count