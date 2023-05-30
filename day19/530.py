class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #inorder: left right root
        diff = float("inf")
        pre = None 
        def traversal(root):
            nonlocal diff,pre
            if root.left:
                traversal(root.left)
            if pre:
                diff = min(diff,abs(root.val - pre.val))
            pre = root
            if root.right:
                traversal(root.right)
            
        traversal(root)
        return diff