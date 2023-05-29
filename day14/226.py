Level order traversal 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #postorder
        if not root:
            return root
        que = deque([root])
        while que:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                cur.left,cur.right = cur.right,cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root


Recursion traversal: post order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


Iteration traversal: post order 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #postorder
        if not root:
            return root
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left,cur.right = cur.right,cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root
        





