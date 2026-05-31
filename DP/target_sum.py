class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp={}
        def dfs(i,sum):
            if (i,sum) in dp:
                return dp[(i,sum)]

            if i==len(nums):
                if sum==target:
                    return 1
                else :
                    return 0
            
            add= dfs(i+1, sum+nums[i])
            sub= dfs(i+1, sum-nums[i])
            dp[(i,sum)]=sub+add
            return add+sub
        
        return dfs(0,0)

        
