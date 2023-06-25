class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i] += dp[i-coin] + coin 
        memo = {}
        def dfs(i,total):
            if total == amount:
                return 1
            if i>=len(coins) or total > amount:
                return 0
            key = (i,total)
            if key in memo:
                return memo[key]
            #memo[(0,0)] = 0
            memo[key] = dfs(i+1,total) + dfs(i,total+coins[i])
            return memo[key]
        return dfs(0,0)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i] += dp[i-coins[j]]
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] += dp[j - coin]
        return dp[-1]