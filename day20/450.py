class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #1. leaf 
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            if root.left and root.right:
                cur  = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
            if not root.left and root.right:
                return root.right
            if root.left and not root.right:
                return root.left
        
        root.left = self.deleteNode(root.left,key)
        
        root.right = self.deleteNode(root.right,key)
        
        return root