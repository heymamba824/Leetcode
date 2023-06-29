class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1,n + 1):
            for word in wordDict:
                length = len(word)
                if i>= length:
                    temp = s[i-length:i]
                    if temp in wordDict and dp[i-length] == True:
                        dp[i] = True
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        words = set(wordDict)
        def dfs(s):
            if len(s) == 0:
                return True
            if s in memo:
                return memo[s]
            for word in words:
                temp = s[:len(word)]
                if temp in words and dfs(s[len(word):]):
                    memo[temp] = True
                    return memo[temp]
            memo[s] = False
            return False
        return dfs(s)            

