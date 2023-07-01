class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #hold the stock 
        #sell the stock
        #sell the stock before 
        #colddown。
        size = len(prices)
        dp = [[0] * 4 for _ in range(size)]
        dp[0][0] = -prices[0]
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0],max(dp[i-1][3],dp[i-1][2])-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1],dp[i-1][2])
            dp[i][3] = dp[i-1][0] - prices[i]
        return max(dp[-1])


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