class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(total):
            if total == n:
                return 1
            if total > n:
                return 0
            if total in memo:
                return memo[total]
            
            memo[total] = dfs(total+1) + dfs(total+2)
            return memo[total]
        
        return dfs(0)