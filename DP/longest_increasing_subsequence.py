#this is to find the longest increasing subsequence, meaning any iteams can be skipped bt the increasing order is always preserved.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(1+dp[j],dp[i])
        
        return max(dp)
