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
        

