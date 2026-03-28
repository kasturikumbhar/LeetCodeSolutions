class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:

        def findLeft(l,r,nums,t):
            f =-1
            while(l<=r):

                mid=l+(r-l)//2
                if nums[mid]==t:
                    f=mid 
                    r=mid-1 #if target found keep searching for left most
                elif(t<nums[mid]):
                    r=mid-1 #not equal to mid bt may be present on left side if smaller than mid 
                else:
                    l=mid+1 #not present on initial left so check right side 
            return f # can directly return mid


    
        def findRight( l,r,nums,t):
            f =-1
            while(l<=r):
                mid=l+(r-l)//2
                if nums[mid]==t:
                    f=mid
                    l=mid+1 #if mid is equal go on to find right most 

                elif(t>nums[mid]):
                    l=mid+1 # not equal to mid so check on right end if greater than mid
                else:
                    r=mid-1
            return f

        if(nums): #if empty then diretcly return -1
            l,r=0,len(nums)-1
           
            return [findLeft(l,r,nums, t), findRight(l, r, nums,t)] #check binary search to be done twice 
        return [-1,-1]


        
