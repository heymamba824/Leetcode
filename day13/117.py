class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                if i == size - 1:
                    cur.next = None
                else:
                    cur.next = que[0]
        return root