class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2 !=0 :
            return False
        target=total//2


        dp={0}
        for i in nums:
            curr_set=set()
            for j in dp:
                curr_set.add(j)
                curr_set.add(j+i)
            dp=curr_set
            if target in dp:
                return True
            
        return False





"""dfs + dp way :
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        print(total)
        if total%2 !=0 :
            return False
        target=total//2
        print(target)

        if target in nums:
            return True

        dp={}
        def dfs(i,remaining ):
            
            if remaining ==0:
                return True
            if i==len(nums) or remaining  < 0:
                return False
            if((i,remaining ) in dp):
                return dp[(i,remaining )]
            add=dfs(i+1,remaining - nums[i])
            skip=dfs(i+1, remaining )
            dp[(i,remaining )]=add or skip
            return dp[(i,remaining )] 
        
        return dfs(0,target)

"""
