class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #cover area 
        if len(nums) == 1 :
            return True
        cover = 0 
        for i in range(len(nums)-1):
            if i <= cover:
                cover = max(cover,nums[i]+i)
                if cover >= len(nums) -1 :
                    return True
        return False