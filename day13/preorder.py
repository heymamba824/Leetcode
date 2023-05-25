Preorder





recursion:

Root 
Root.left
root.right



Iteration:

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traversal(root):
            if not root:
                return None 
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return result 


Stack

Root

root.right

Root.left


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        if not root:
            return []
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result   