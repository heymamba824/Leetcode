class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        size1 = len(s)
        size2 = len(t)
        dp = [[0]*(size2 + 1) for _ in range(size1 + 1)]
        for i in range(size1):
            dp[i][0] = 1
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(n,m):
            key = (n,m)
            if n == len(s):
                return int(m==len(t))
            if m == len(t):
                return 1
            if key in memo:
                return memo[key]
            if s[n] == t[m]:
                memo[key] = dfs(n+1,m+1) + dfs(n+1,m)
            else:
                memo[key] = dfs(n+1,m)
            return memo[key]
        return dfs(0,0)