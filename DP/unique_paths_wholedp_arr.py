class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)] # this is required as dp=[[1]*n]*m forms referenced rows and any udpate to 1 row reflects to other .. thus make it value based instead of reference based
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        print(dp)
        return dp[m-1][n-1]   
