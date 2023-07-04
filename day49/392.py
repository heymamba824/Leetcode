class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size1 = len(s)
        size2 = len(t)
        # dp[i][j]: the number of same part of s and t
        dp = [[0] * (size2+1) for _ in range(size1+1)]
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[-1][-1] == size1:
            return True
        else:
            return False

