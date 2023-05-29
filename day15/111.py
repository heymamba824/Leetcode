class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        if not root.left and not root.right:
            return 1 
        left = float("inf")
        right = float("inf")
        if root.left:
            left = min(left,self.minDepth(root.left))
        if root.right:
            right = min(right,self.minDepth(root.right))
        return 1 + min(left,right)




class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root])
        depth = 0
        while que:
            size = len(que)
            depth += 1
            for _ in range(size):
                cur = que.popleft()
                #print(depth)
                if not cur.left and not cur.right:
                    return depth 
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                #max_depth = max(max_depth,depth)
        return depth 