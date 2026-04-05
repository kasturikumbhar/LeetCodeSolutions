import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        heap=[]
        print(counts.items())
        for num,freq in counts.items():
            heapq.heappush(heap, (freq,num) )
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]
        # c=sorted(c,key=c.get,reverse=True) 
        # return c[:k]
 

