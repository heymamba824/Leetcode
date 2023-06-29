class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #dp
        def traversal(root):
            if not root:
                return (0,0)
            left = traversal(root.left)
            right = traversal(root.right)
            val0 = max(left[0],left[1]) + max(right[0],right[1])
            val1 = root.val + left[0] + right[0]
            return (val0,val1)
        return max(traversal(root))

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #dp
        memo = {}
        def traversal(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            if root in memo:
                return memo[root]
            val1 = root.val
            if root.left:
                val1 += traversal(root.left.left) + traversal(root.left.right)
            if root.right:
                val1 += traversal(root.right.left) + traversal(root.right.right)
            val2 = traversal(root.left) + traversal(root.right)
            memo[root] = max(val1,val2)
            return memo[root]
        return traversal(root)