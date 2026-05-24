class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        
        
        def rob_linear( arr):
            n=len(arr)
            if n==1:
                return arr[0]
            if n==2:
                return max(arr[0],arr[1])
            prev2=arr[0]
            prev1=max(arr[0],arr[1])
            for i in range(2, n):
                curr=max(prev1, arr[i]+prev2)
                prev2=prev1
                prev1=curr
            return prev1
        
        return max(rob_linear(nums[0:-1]), rob_linear(nums[1:]))


        
