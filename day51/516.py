class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(l,r):
            key = (l,r)
            if key in memo:
                return memo[key]
            if l > r :
                return 0
            if l == r :
                return 1
            if s[l] == s[r]:
                memo[key] = dfs(l+1,r-1) + 2
            else:
                memo[key] = max(dfs(l+1,r),dfs(l,r-1))
            return memo[key]
        return dfs(0,len(s)-1)