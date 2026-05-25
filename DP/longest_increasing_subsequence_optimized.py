#O(nlogn)
# maintain a tail array instead of O(n2) dp 2D array
# if new ele is greater then append otherwise perform binary search on tail to fnid idex to  replace the new element at
#use python bisect module >> bisect.bisect_left(arr, target) returns index .. replace value of this index with curr value
#return len of this tail array tail defines the longest increasing subsequence possible

import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n=len(nums)
        # dp=[1]*n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             dp[i]=max(1+dp[j],dp[i])
        
        # return max(dp)
        tail=[]
        for n in nums:
            if not tail or n > tail[-1]:
                tail.append(n)
            else:
                idx=bisect.bisect_left(tail,n)
                tail[idx]=n
        
        return len(tail)




        
