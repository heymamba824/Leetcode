class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        re = []
        path = [ ]
        if not root:
            return []
        def traversal(root,val):
            if not root.left and not root.right:
                if val == 0:
                    re.append(path[:])
                return
            if root.left:
                path.append(root.left.val)
                traversal(root.left,val - root.left.val)
                path.pop()

            if root.right:
                path.append(root.right.val)
                traversal(root.right,val - root.right.val)
                path.pop()
        path.append(root.val)
        traversal(root,targetSum-root.val)
        return re 


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        re = []
        path_way = []
        stack = [(root,root.val)]
        path_way.append([root.val])
        while stack:
            cur,val = stack.pop()
            path = path_way.pop()
            if not cur.left and not cur.right and val == targetSum:
                re.append(path)
            if cur.left:
                stack.append((cur.left,val + cur.left.val))
                path_left = path + [cur.left.val]
                #path_way.append(path+[cur.left.val])
                path_way.append(path_left)
            if cur.right:
                stack.append((cur.right,val+cur.right.val))
                path_right = path + [cur.right.val]
                #path_way.append(path+[cur.right.val])
                path_way.append(path_right)
        return re 