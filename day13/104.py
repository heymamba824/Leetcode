


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #inorder
        if not root:
            return 0 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        height = max(left,right) + 1
        return height 



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0 
        que = deque([root])
        while que:
            depth += 1
            for _ in range(len(que)):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
        return depth
        