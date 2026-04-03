# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, p : Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def sametree(p,q):
 
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return sametree(p.left,q.left) and sametree(p.right,q.right)

        
        def ispresent(p,q):
            if p is None:
                return False

            if sametree(p,q):
                return True
            
            return ispresent(p.left,q) or ispresent(p.right,q)

        
        return ispresent(p,q)
        
       
