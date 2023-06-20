class Solution:
    def integerBreak(self, n: int) -> int:
        #dp[i] = max(dp[i],max(dp[i-j]*j,(i-j)*j))
        memo = {}
        def dfs(n):
            if n == 2:
                return 1 
            if n < 2:
                return 0 
            if n in memo:
                return memo[n]
            total = 0
            for j in range(2,n):
                total = max(total,dfs(n-j)*j,(n-j)*j)
            memo[n] = total 
            return total
        return dfs(n)