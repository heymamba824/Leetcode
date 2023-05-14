class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        for i in range(1,len(prices)):
            result += max(0,prices[i] - prices[i-1])
        return result




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        size = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1, size):
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])
        return dp0