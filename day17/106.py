class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        #inorder  left  root right 
        #postorder left right root
        if not inorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        
        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]

        root.left = self.buildTree(inorder_left,postorder_left)
        root.right = self.buildTree(inorder_right,postorder_right)
        return root