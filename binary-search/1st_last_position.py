class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findstartpos(nums,target):
            left=0
            right=len(nums)
            while left<right:
                mid=(left+right)//2
                if target>nums[mid]:
                    left=mid+1
                else:
                    right=mid
            return left
        
        l=findstartpos(nums,target)
        r=findstartpos(nums,target+1) -1
        if l==len(nums) or nums[l]!=target:
            return [-1,-1]
        else: 
            return[l,r]

        

        
