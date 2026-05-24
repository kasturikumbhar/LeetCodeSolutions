class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ans=stack.pop()
                answer[ans]=i-ans 
            stack.append(i)
        return answer


        
