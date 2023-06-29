class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] hold the stock 
        # dp[i][1] do not hold the stock
        # dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        # dp[i][0] = max(dp[i-1][0], -prices[i])
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1,len(prices)):
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
            dp[i][0] = max(dp[i-1][0], -prices[i])
        return dp[-1][1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] hold the stock 
        # dp[i][1] do not hold the stock
        # dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        # dp[i][0] = max(dp[i-1][0], -prices[i])
        dp0 = -prices[0]
        dp1 = 0
        for i in range(1,len(prices)):
            dp0 = max(dp0,-prices[i])
            dp1 = max(dp1, dp0+prices[i])
        return dp1


