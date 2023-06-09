class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        count = 1 
        for i in range(len(nums)-1):
            cur = nums[i+1] - nums[i]
            if pre*cur <= 0 and cur!=0:
                pre = cur 
                count +=1
        return count