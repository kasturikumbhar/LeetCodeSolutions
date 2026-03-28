# Pattern: Binary Search on Rotated Array
# Time: O(log n) | Space: O(1)
# Leetcode #33 - Search in Rotated Sorted Array
# Status: Accepted ✅
class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            mid=l+(r-l)//2
            if(nums[mid]==t):
                return mid
            if (nums[mid]>=nums[l]): #indicates left side of array is sorted then check if target present 
                if(nums[l] <= t <= nums[mid]):
                    r=mid-1
                else:
                    l=mid+1
            else: #now its right side sorted, again check if target present in this side 
                if((nums[mid]<=t<=nums[r])):
                    l=mid+1
                else:
                    r=mid-1
            
        return -1

        
