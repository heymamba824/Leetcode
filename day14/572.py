class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traversal(root):
            if not root:
                return False
            if root.val == subRoot.val:
                return compare(root,subRoot)
            return traversal(root.left) or traversal(root.right)
        def compare(root,subroot):
            if not tree1 and not tree2:
                return True
            elif tree1 and not tree2:
                return False
            elif not tree1 and tree2:
                return False 
            elif tree1.val != tree2.val:
                return False 
            outside = compare(tree1.left,tree2.left)
            inside = compare(tree1.right,tree2.right)
            result = outside and inside
            return result
            
        return traversal(root)