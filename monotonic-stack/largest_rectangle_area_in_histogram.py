class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[]
        maxarea=0

        for i,height in enumerate(heights):
            while stack and height <heights[stack[-1]]:
                stacktop=stack.pop()
                leftboundary= stack[-1] if stack else -1 ## leftboundary is prev block
                area=heights[stacktop]* (i-leftboundary-1) 
                maxarea=max(maxarea,area)
            stack.append(i)
        return maxarea
        
