class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False] *(size+1)
        dp[0] = True
        for i in range(1,size+1):
            for word in wordDict:
                length = len(word)
                if word == s[i-length:i] and dp[i-length] == True:
                    dp[i] = True
                    break
        return dp[size]