class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traversal(root):
            if not root:
                return 0 
            left = traversal(root.left)
            right = traversal(root.right)
            if left == -1:
                return -1
            if right == -1:
                return -1 
            if abs(left-right) > 1:
                return -1 
            else:
                return 1 + max(left,right)
        re = traversal(root)
        if re == -1 :
            return False
        else:
            return True