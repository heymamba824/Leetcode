class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i]: the lowest cost to arrive at ith stairs
        # dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        dp0 = 0
        dp1 = 0
        for i in range(2,len(cost)+1):
            temp = min(dp0+cost[i-2],dp1 + cost[i-1])
            dp0 = dp1
            dp1 = temp
        return dp1