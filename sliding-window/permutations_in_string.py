from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_c=Counter(s1)
        res=Counter()
        left=0
        for right in range(len(s2)):
            res[s2[right]]=1+res.get(s2[right],0)
            while(right-left+1 > len(s1)):
                res[s2[left]]-= 1
                if res[s2[left]]==0:
                    del res[s2[left]]
                left+=1
            if(res==s1_c):
                return True
        return False 
            
        
