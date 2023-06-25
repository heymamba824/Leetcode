class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(total):
            if total == amount:
                return 0
            if total > amount:
                return -1
            if total in memo:
                return memo[total]

            k = float('inf')
            for coin in coins:
                res = dfs(total + coin)
                if res != -1:
                    k = min(k, res + 1)
            memo[total] = k if k != float('inf') else -1
            return memo[total]

        return dfs(0)