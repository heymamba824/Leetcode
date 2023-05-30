class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #inorder 
        max_val = -float("inf")
        def traversal(root):
            nonlocal max_val
            if not root:
                return True
            left = traversal(root.left)
            if root.val > max_val:
                max_val = root.val
            else:
                return False
            right = traversal(root.right)
            return left and right
        return traversal(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #inorder 
        if not root:
            return True
        stack = []
        cur = root
        pre = None
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and cur.val < pre.val:
                    return False
                pre = cur 
                cur = cur.right
        return True