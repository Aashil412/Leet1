class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, i,j):
            if(i >= 0 and i <= len(grid)-1 and j >= 0 and  j <= len(grid[0])-1 and grid[i][j] == '1'):
                grid[i][j]=0
                bfs(grid, i+1,j)
                bfs(grid,i-1,j)
                bfs(grid,i,j+1)
                bfs(grid,i,j-1)
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == '1'):
                    bfs(grid,i,j)
                    counter+=1
        
        return counter    