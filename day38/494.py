class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i,total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0 
            key = (i,total)
            if key in memo:
                return memo[key]
            memo[key] = dfs(i+1,total+nums[i]) + dfs(i+1,total-nums[i])
            return memo[key]
        return dfs(0,0)