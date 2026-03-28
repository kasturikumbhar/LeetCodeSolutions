# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if  root is None:
            return []
        result =[]
        q=deque() #ds for level order traversal
        q.append(root)
        while(q):
            size=len(q) # determines no of nodes at that level that would be size of l that gets appended to the result 
            l=[]
            for i in range(size):
                node=q.popleft()
                l.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            result.append(l)
        return result

                
            
                

