class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        left = self.hasPathSum(root.left,targetSum-root.val)
        right = self.hasPathSum(root.right,targetSum-root.val)
        return left or right



class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root,0)]
        while stack:
            cur,val = stack.pop()
            val += cur.val
            if not cur.left and not cur.right and val == targetSum:
                return True
            if cur.left:
                stack.append((cur.left,val))
            if cur.right:
                stack.append((cur.right,val))
        return False