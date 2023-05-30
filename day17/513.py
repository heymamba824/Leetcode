Level order:
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        re = 0
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if i == 0:
                    re = cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return re 

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -float('inf')
        re = 0 
        def traversal(root,depth):
            nonlocal max_depth,re
            if not root:
                return 
            if not root.left and not root.right:
                if depth > max_depth:
                    re = root.val 
                    max_depth = depth 
            traversal(root.left,depth+1)
            traversal(root.right,depth+1)
        traversal(root,0)
        return re 