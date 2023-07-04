class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp[i]: the max sum of nums[:i]
        size = len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        re = nums[0]
        for i in range(1,size):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            re = max(re,dp[i])
        return re

