class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #right root left
        pre = 0 
        def traversal(root):
            if not root:
                return None
            nonlocal pre
            traversal(root.right)
            root.val += pre
            pre = root.val 
            traversal(root.left)
            return root 
        return traversal(root)