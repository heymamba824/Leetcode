class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[n] : the number of solutions to get amount
        dp = [0] *(amount + 1)
        #initialize 
        dp[0] = 1
        #format   dp[n] += max(dp[n-conis[i]])
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] += dp[j-coin]

        return dp[amount]