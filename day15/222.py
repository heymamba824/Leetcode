class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left_depth,right_depth = 0,0 
        left = root.left
        right = root.right
        while left:
            left_depth += 1
            left = left.left
        while right:
            right_depth += 1
            right = right.right
        if left_depth == right_depth:
            return   2**(left_depth+1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right) 