class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traversal(root,depth):
            if not root:
                return None
            if depth == len(result):
                result.append(root.val)
            traversal(root.right,depth+1)
            traversal(root.left,depth+1)
        traversal(root,0)
        return result 