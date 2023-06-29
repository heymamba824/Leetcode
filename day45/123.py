class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][0]:first buy
        #dp[i][1]: first sell
        #dp[i][2] : second buy
        #dp[i][3]: second sell
        size = len(prices)
        dp = [[0] * 4 for _ in range(size)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = -prices[0]
        dp[0][3] = 0
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0],-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i][0]+prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i][1]-prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i][2]+prices[i])
        return dp[-1][-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][0]:first buy
        #dp[i][1]: first sell
        #dp[i][2] : second buy
        #dp[i][3]: second sell
        size = len(prices)
        #dp = [[0] * 4 for _ in range(size)]
        dp0= -prices[0]
        dp1 = 0
        dp2 = -prices[0]
        dp3 = 0
        for i in range(1,size):
            dp0 = max(dp0,-prices[i])
            dp1 = max(dp1,dp0+prices[i])
            dp2 = max(dp2,dp1-prices[i])
            dp3 = max(dp3,dp2+prices[i])
        return dp3


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][0]:first buy
        #dp[i][1]: first sell
        #dp[i][2] : second buy
        #dp[i][3]: second sell
        size = len(prices)
        memo = {}
        def dfs(i,bought,time):
            if i == size or time == 2:
                return 0
            key = (i,bought,time)
            if key in memo:
                return memo[key]
            
            if bought:
                memo[key] = max(dfs(i+1,False,time+1)+prices[i],dfs(i+1,True,time))
            else:
                memo[key] = max(dfs(i+1,True,time)-prices[i],dfs(i+1,False,time))
            return memo[key]
        return dfs(0,False,0)