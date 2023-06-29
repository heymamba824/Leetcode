class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[n] = max(dp[n-1],dp[n-2]+nums[n])
        if len(nums) == 1:
            return nums[0]
        prev = 0
        cur = 0
        for num in nums:
            temp = cur
            cur = max(prev+num,cur)
            prev = temp
        return cur 


class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp [n] = max(dp[n-1],dp[n-2]+nums[n])
        #dp [0] = nums[0]
        #dp[1] = max(nums[0],nums[1])
        if len(nums) ==1 :
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[n] = max(dp[n-1],dp[n-2]+nums[n])
        memo = {}
        def dfs(n):
            if n <0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = max(dfs(n-1),dfs(n-2)+nums[n])
            return memo[n]
        return dfs(len(nums)-1)