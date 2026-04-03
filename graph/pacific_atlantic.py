class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if  heights is None:
            return 
        
        pacific = set()
        atlantic=set()

        r=len(heights)
        c=len(heights[0])

       
        def dfs(heights, ocean, i,j,previous):
            if i<0 or i>r-1 or j<0 or j>c-1 or heights[i][j]<previous or (i,j) in ocean:
                return 
            
            if (i,j) not in ocean and heights[i][j]>=previous:
                ocean.add((i,j))

            dfs(heights,ocean,i+1,j, heights[i][j])
            dfs(heights,ocean,i-1,j, heights[i][j])
            dfs(heights,ocean,i,j+1, heights[i][j])
            dfs(heights,ocean,i,j-1, heights[i][j])
        
        for i in range(r):
            dfs(heights, pacific,i,0,heights[i][0])
            dfs(heights, atlantic,i,c-1,heights[i][c-1])
        
        for j in range(c):
            dfs(heights, pacific,0,j,heights[0][j])
            dfs(heights, atlantic,r-1,j,heights[r-1][j])
        

        return list(pacific & atlantic)



        



        
        
