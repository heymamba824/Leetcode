class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        index = inorder.index(root_val)

        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]

        preorder_left = preorder[1 :len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        root.left = self.buildTree(preorder_left,inorder_left)
        root.right = self.buildTree(preorder_right,inorder_right)

        return root