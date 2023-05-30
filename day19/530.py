class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #inorder: left right root
        diff = float("inf")
        pre = None 
        def traversal(root):
            nonlocal diff,pre
            if root.left:
                traversal(root.left)
            if pre:
                diff = min(diff,abs(root.val - pre.val))
            pre = root
            if root.right:
                traversal(root.right)
            
        traversal(root)
        return diff


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #inorder: left right root
        if not root:
            return 0
        stack =[]
        cur = root
        pre = None
        re = float("inf")
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    re = min(re,abs(pre.val-cur.val))
                pre = cur 
                cur = cur.right
        return re 