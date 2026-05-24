class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest=0
        j=0
        left=right=0
        while right<len(nums)-1:
            for i in range(left,right+1):
                farthest=max(farthest,i+nums[i])
            j+=1
            left=right+1
            right=farthest

        return j


        
