class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[0]: hold the stock
        #dp[1]: sell the stock today
        #dp[2]: sell the stock before
        #dp[3]: colddown
        if len(prices) == 0:
            return 0
        dp = [0]*4
        dp[0] = -prices[0]
        pre = dp[:]
        for i in range(1,len(prices)):
            dp[0] = max(dp[0],max(pre[2],dp[3])-prices[i])
            dp[1] = pre[0] + prices[i]
            dp[2] = max(pre[2],pre[3])
            dp[3] = pre[1]
            pre = dp[:]
        return max(dp[1],dp[2],dp[3])