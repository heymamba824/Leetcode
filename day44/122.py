class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = -prices[0]
        dp1 = 0
        for i in range(1,len(prices)):
            dp0 = max(dp1-prices[i],dp0)
            dp1 = max(dp0+prices[i],dp1)
        return dp1


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,buy):
            if i == len(prices):
                return 0 
            key = (i,buy)
            if key in memo:
                return memo[key]   
            if buy:
                memo[key] = max(dfs(i+1,False) + prices[i],dfs(i+1,True))
            else:
                memo[key] = max(dfs(i+1,True) - prices[i],dfs(i+1,False))
            return memo[key]
        return dfs(0,False)