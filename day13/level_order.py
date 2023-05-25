Iteration:
Deque
1.count the size of every level
2.popleft


Recursion:
1.depth
2. result[depth].append(root.val)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def traversal(root,depth):
            if not root:
                return None
            if len(result) == depth:
                result.append([])
            result[depth].append(root.val)
            traversal(root.left,depth+1)
            traversal(root.right,depth+1)
        traversal(root,0)
        return result

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []
        que = deque([root])
        while que:
            size = len(que)
            re = []
            for _ in range(size):
                cur = que.popleft()
                re.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(re)
        return results
