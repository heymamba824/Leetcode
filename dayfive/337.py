# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traversal(root):
            if not root:
                return (0,0)
            left = traversal(root.left)
            right = traversal(root.right)
            val_1 = root.val +  left[0] + right[0]
            val_0 = max(left[0],left[1]) + max(right[0],right[1])
            return (val_0,val_1)
        return max(traversal(root))