class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        que = deque()
        que.append(p)
        que.append(q)
        while que:
            left = que.popleft()
            right = que.popleft()
            if not left or not right or left.val != right.val:
                return False
            if left.val == right.val:
                continue 
            que.append(left.left)
            que.append(right.left)
            que.append(left.right)
            que.append(right.right)
        return True  