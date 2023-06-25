class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(total):
            if total > target:
                return 0
            if total == target:
                return 1
            if total in memo:
                return memo[total]

            memo[total] = 0  # Initialize memo[total] to 0 before the loop
            for num in nums:
                memo[total] += dfs(total + num)
            return memo[total]

        return dfs(0)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1,target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
                
        return dp[-1]