class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0 
        re = 0 
        for num in nums:
            count += num
            if count > re:
                re = count  
            if count <= 0:
                count = 0
        return re