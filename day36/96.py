class Solution:
    def numTrees (self, n: int) -> int:
        dp = [0] *(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]


class Solution:
    def numTrees (self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n<=1:
                return 1
            if n in memo:
                return memo[n]
            total = 0
            for j in range(n):
                total += dfs(n-1-j) * dfs(j)
            memo[n] = total
            return total
        return dfs(n)
        