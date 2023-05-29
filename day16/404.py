class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #postorder
        if not root:
            return 0 
        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        val = 0 
        if root.left and not root.left.left and not root.left.right:
            val = root.left.val
        return val + left + right