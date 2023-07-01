class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #dp[i][0]: hold the stock
        #dp[i][1]: do not hold the stock
        size = len(prices)
        dp = [[0] * 2 for _ in range(size)]
        dp[0][0] = -prices[0]
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i]-fee)
        return dp[-1][-1]