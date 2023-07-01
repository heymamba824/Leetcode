class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = len(prices)
        memo = {}
        def dfs(i,bought,time):
            if i == size or time == k:
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
        

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #dp[i][0]:  hold the stock 
        #dp[i][1]: buy the stock
        #dp[i][2]: sell the stock  
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        for i in range(1,2*k,2):
            dp[0][i] = -prices[0]
        for i in range(1,len(prices)):
            for j in range(0,2*k,2):
                dp[i][0] = dp[i-1][0]
                dp[i][j+1] = max(dp[i-1][j+1],dp[i-1][j]-prices[i])
                dp[i][j+2] = max(dp[i-1][j+2],dp[i-1][j+1]+prices[i])
        return dp[-1][-1]
