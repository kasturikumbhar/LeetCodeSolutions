class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start=end=0
        last={}
        partition=[]
        for i in range(len(s)):
            last[s[i]]=i
        
        for i in range(len(s)):
            end= max(end, last[s[i]])
            if i==end:
                partition.append(end-start+1)
                start=i+1
        
        return partition
            
