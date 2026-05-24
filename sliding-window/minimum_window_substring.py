from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_c=Counter(t)
        window={}
        required=len(t_c)
        formed=0
        left=0
        bestlen=float('inf')
        best=[0,0]

        for right in range(len(s)):
            ch=s[right]
            window[s[right]]=1+window.get(s[right],0)
            if ch in t_c and window[ch]==t_c[ch]:
                formed+=1 
            while formed==required:
                if right-left+1 < bestlen:
                    bestlen=(right-left+1)
                    best=[left,right]
                ch_l=s[left]
                left+=1
                window[ch_l]-=1
                if ch_l in t_c and window[ch_l]<t_c[ch_l]:
                    formed-=1
        
        l,r=best
        return s[l:r+1] if bestlen!=float('inf') else ""

                

                
        
