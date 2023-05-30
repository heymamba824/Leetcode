class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val > val:
            return self.searchBST(root.left,val)
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right,val)