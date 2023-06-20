class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1 :
            return False
        dp = [0] * (target+1)
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j] = max(dp[j],dp[j-num]+num)
                if dp[j] == target //2:
                    return True
        return False



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        memo = {}
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i ==len(nums):    
                return False
            if (i,target) in memo:
                return memo[(i,target)]
            return dfs(i+1, target) or dfs(i+1, target - nums[i])
            
        return dfs(0, target//2)