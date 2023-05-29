class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #inorder
        def traversal(root,path):
            #print(path)
            path += str(root.val)
            if not root.left and not root.right:
                re.append(path)
            if root.left:
                traversal(root.left,path+'->') 
            if root.right:
                traversal(root.right,path+'->')
        if not root:
            return []
        re = []
        traversal(root,'')
        return re



class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        stack = [root]
        path_way = []
        re = []
        path_way.append(str(root.val))
        while stack:
            cur  = stack.pop()
            path = path_way.pop()
            if not cur.left and not cur.right:
                re.append(path)
            if cur.right:
                stack.append(cur.right)
                path_way.append(path+'->'+str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_way.append(path+'->'+str(cur.left.val))

        return re