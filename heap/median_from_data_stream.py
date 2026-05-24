import heapq
class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        if len(self.minheap)==len(self.maxheap)==0 or num<= -self.maxheap[0]:
            heapq.heappush(self.maxheap,-num)
            if len(self.maxheap)> len(self.minheap)+1:
                maxtop=-heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap,maxtop)
        else:
            heapq.heappush(self.minheap,num)
            if len(self.minheap)>len(self.maxheap)+1:
                mintop=heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap,-mintop)       



    def findMedian(self) -> float:
        if len(self.maxheap)> len(self.minheap):
            return-self.maxheap[0]
        elif(len(self.maxheap)< len(self.minheap)):
            return self.minheap[0]
        else:
            return(-self.maxheap[0]+self.minheap[0])/2
        

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
