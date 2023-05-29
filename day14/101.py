class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #postorder
        if not root:
            return True
        que = deque()
        que.append(root.left)
        que.append(root.right)
        while que:
            left = que.popleft()
            right = que.popleft()
            if not left or not right or left.val != right.val:
                return False
            if left.val == right.val:
                continue
            que.append(left.left)
            que.append(right.right)
            que.append(left.right)
            que.append(right.left) 
        return True 


