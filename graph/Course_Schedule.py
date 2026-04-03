from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #kanhs algo >> find indegree of all nodes, update q with all independent nodes, now pop left then check for add to result as this is the one with 0 indegree can be finished, next check for its nieghbors reduce  indegree of neigs n then check if indegree is 0 its eligible to be added to q n to result n next node again check for its neis n continue n at the enc check if no of courses in result n actual are same or not .
        grid={i :[] for i in range(numCourses) }
        indegree=[0 for i in range(numCourses)]
        
        for course,prereq in prerequisites:
            grid[prereq].append(course)
            indegree[course]+=1
       
        q=deque()
        result=[]
        for i in range(numCourses):
            if indegree[i] ==0:
                q.append(i)
        
        while q:

            node=q.popleft()
            result.append(node)
            for nei in grid[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
            
        
        return len(result)==numCourses


