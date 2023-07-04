class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]: the increasing subsequence of nums[:i]
        dp = [1] * len(nums)
        result = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
            result = max(result,dp[i])
        return result


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(n):
            if n == len(nums):
                return 0 
            if n in memo:
                return memo[n]
            re = 1  # LIS length ending at index n is at least 1 (the element itself)
            for i in range(n):
                if nums[n] > nums[i]:
                    re = max(re, dfs(i)+1)  # update the LIS length ending at index n
            memo[n] = re 
            return re
        return max(dfs(i) for i in range(len(nums)))