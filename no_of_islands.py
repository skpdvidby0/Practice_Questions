class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count =0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    self.gridDFS(i,j,grid)
                    count+=1
        return count
    def gridDFS(self,i,j,grid):
        if i<0 or j<0 or i>len(grid) or j>len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j]='#'
        self.gridDFS(i+1,j,grid)
        self.gridDFS(i-1,j,grid)
        self.gridDFS(i,j+1,grid)
        self.gridDFS(i,j-1,grid)