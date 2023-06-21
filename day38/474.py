class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #dp[i][j], the number of '0' and '1'

        memo = {}
        def dfs(i,zero,one):
            if zero < 0 or one < 0:
                return -1
            if i == len(strs):
                return 0
            if i == len(strs):
                return 0
            key = (i,zero,one)
            if key in memo:
                return memo[key]
            memo[key] = max(dfs(i+1,zero,one),1+dfs(i+1,zero-strs[i].count('0'),one-strs[i].count('1')))
            return memo[key]
        return dfs(0,m,n)