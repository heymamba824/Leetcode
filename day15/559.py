class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0 
        depth = 0 
        for child in root.children:
            depth = max(depth,self.maxDepth(child))
        return 1 + depth   



class Solution:
    def maxDepth(self, root: 'Node') -> int:
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
                for child in cur.children:
                    que.append(child)
                #max_depth = max(max_depth,depth)
        return depth 