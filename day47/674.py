class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 1 
        size = len(nums)
        dp = [1] * size
        for i in range(1,size):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            result = max(result,dp[i])
        return result 


