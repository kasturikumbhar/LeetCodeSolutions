class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j ,grid):
            if i<0 or i>=r or j<0 or j>=c or  grid[i][j]=='0':
                return

            grid[i][j]='0'
            dfs(i+1,j,grid)
            dfs(i-1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)  
        
        if not grid:
            return 0
        
        r,c=len(grid) , len(grid[0])
        count =0
        for i in range(r):
            for j in range(c):
                print(i,j)

                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j,grid)
        
        return count

        
