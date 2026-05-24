class Solution:
    def climbStairs(self, n: int) -> int:
        prev1=1 #step 0
        prev2=1 #step 1
        curr=0
        if n <2:
            return n
        for i in range(1,n+1): #n+1 as we need to check till nth stair
            if i <2:
                continue
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        
        return curr
        
