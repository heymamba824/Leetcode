class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = 0 
        max_count = 0 
        pre = None
        result = []
        def traversal(root):
            nonlocal count,max_count,pre,result
            if not root:
                return 
            traversal(root.left)
            if pre:
                if pre.val == root.val:
                    count += 1
                else:
                    count = 1
            else:
                count = 1
            print(count,max_count)
            if count == max_count:
                result.append(root.val)
            elif count > max_count:
                result = [root.val]
                max_count = count
            
            pre = root
            traversal(root.right)
        traversal(root)
        return result



class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
           return []
        result = []
        times = 0
        stack = []
        cur = root
        pre = None
        max_time = 0 
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    if pre.val == cur.val:
                        times += 1
                    else:
                        times = 1
                else:
                    times = 1
                if times == max_time:
                    result.append(cur.val)
                elif times> max_time:
                    max_time = times
                    result = [cur.val]
                pre = cur
                cur = cur.right
        return result 