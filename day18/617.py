if not root1 and root2:
            return root2
        if root1 and not root2:
            return root1 
        if not root1 and not root2:
            return 
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)
        return root1


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        que = deque()
        que.append(root1)
        que.append(root2)
        while que:
            cur1 = que.popleft()
            cur2 = que.popleft()
            cur1.val += cur2.val
            if cur1.left and cur2.left:
                que.append(cur1.left)
                que.append(cur2.left)
            if cur1.right and cur2.right:
                que.append(cur1.right)
                que.append(cur2.right)
            if not cur1.left and cur2.left:
                cur1.left = cur2.left
            if not cur1.right and cur2.right:
                cur1.right = cur2.right
        return root1