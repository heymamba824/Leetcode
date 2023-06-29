class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            size = len(nums)
            if size == 1:
                return nums[0]
            dp = [0] * size
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,size):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]),helper(nums[:-1]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        #memo = {}
        def dfs(n, nums, memo):
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            if n == 0:
                memo[n] = nums[0]
            elif n == 1:
                memo[n] = max(nums[0], nums[1])
            else:
                memo[n] = max(dfs(n-1, nums, memo), dfs(n-2, nums, memo)+nums[n])
            return memo[n]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(dfs(len(nums)-2, nums[:-1], {}), dfs(len(nums)-2, nums[1:], {}))