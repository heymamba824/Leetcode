class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        index = len(nums)//2
        root = TreeNode(nums[index])
        root.left = self.sortedArrayToBST(nums[:index])
        root.right = self.sortedArrayToBST(nums[index+1:])
        return root