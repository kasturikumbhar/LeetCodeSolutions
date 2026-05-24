class Solution:
    def climbStairs(self, n: int) -> int:
        prev1=1 #step 0
        prev2=1 #step 1
        curr=0
        if n==0 or n==1:
            return 1
        for i in range(2,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        
        return curr
        
