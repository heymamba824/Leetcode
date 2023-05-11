class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = 100001
        left = 0 
        right = 0
        total = 0 
        while right < len(nums):
            total += nums[right]
            while total >= target:
                length = min(length,right - left + 1)
                total -= nums[left]
                left += 1
                
            right += 1
        if length == 100001:
            return 0 
        else:
            return length
