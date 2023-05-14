class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[0]: do nothing
        #dp[1]: first time to hold the stock
        #dp[2]: first time to sell the stock
        #dp[3]: second time to hold the stock
        #dp[4]: second time tp sell the stock
        dp = [0] * 5
        dp[0] = 0
        dp[1] = -prices[0]
        dp[2] = 0
        dp[3] = -prices[0]
        dp[4] = 0
        for i in range(1,len(prices)):
            dp[1] = max(dp[1],dp[0]-prices[i])
            dp[2] = max(dp[2],dp[1]+prices[i])
            dp[3] = max(dp[3],dp[2]-prices[i])
            dp[4] = max(dp[4],dp[3]+prices[i])
        return dp[4]