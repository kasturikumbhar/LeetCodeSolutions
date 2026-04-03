class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        res=0

        def dfs(root):
            if root is None:
                return 0
            
            l=dfs(root.left)
            r=dfs(root.right)

            nonlocal res
            res=max(res,l+r)

            return 1+max(l,r)

        dfs(root)
        return res


