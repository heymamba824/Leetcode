class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # insert = delete
        # dp[i][j] = min(dp[i-1][j-1]+1,)
        size1 = len(word1)
        size2= len(word2)
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]
        for i in range(size1 + 1):
            dp[i][0] = i 
        for j in range(size2 + 1):
            dp[0][j] = j
        for i in range(1,size1 + 1):
            for j in range(1, size2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(n, m):
            if n == len(word1) and m == len(word2):
                return 0
            if n == len(word1):
                return len(word2) - m
            if m == len(word2):
                return len(word1) - n
            key = (n,m)
            if key in memo:
                return memo[key]
            if word1[n] == word2[m]:
                ans = dfs(n+1,m+1)
            else:
                insert = 1 + dfs(n+1, m)
                delete = 1 + dfs(n, m+1)
                replace = 1 + dfs(n+1, m+1)
                ans = min(insert, delete, replace)
            memo[key] = ans
            return memo[key]
        return dfs(0, 0)

