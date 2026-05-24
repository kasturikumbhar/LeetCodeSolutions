from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        maxlen=0
        maxfreq=0
        count={}
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            maxfreq=max(maxfreq,count[s[right]])

            while(((right-left+1) - maxfreq )> k):
                count[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        
        return maxlen



        
