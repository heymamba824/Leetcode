class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1 = len(word1)
        size2 = len(word2)
        # dp = dp[i-1][j-1] ,  dp[i-1][j] + 1
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]
        for i in range(size1+1):
            dp[i][0] = i
        for i in range(size2+1):
            dp[0][i] = i
        for i in range(1,size1 + 1):
            for j in range(1,size2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1,dp[i][j-1]+1,dp[i-1][j-1]+2)
        return dp[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(n,m):
            if n == len(word1) or m == len(word2):
                return 0
            key = (n,m)
            if key in memo:
                return memo[key]
            if word1[n] == word2[m]:
                memo[key] = dfs(n+1,m+1) + 1
            else:
                memo[key] = max(dfs(n+1,m),dfs(n,m+1))
            return memo[key]
        return len(word1) + len(word2) - 2 * dfs(0,0)