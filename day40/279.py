class Solution:
    def numSquares(self, n: int) -> int:
        #target = 
        nums = [i**2 for i in range(1, n + 1) if i**2 <= n]
        dp =[1000000] * (n+1)
        dp[0] = 0
        for num in nums:
            for j in range(num,n+1):
                dp[j] = min(dp[j],dp[j-num]+1)
        return dp[-1]


class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def dfs(total):
            if total == n:
                return 0
            if total > n:
                return float("inf")
            if total in memo:
                return memo[total]
            min_squares = float("inf")
            i = 1 
            while i * i <= n:
                min_squares = min(min_squares, dfs(total + i*i)+1)
                i += 1
            memo[total] = min_squares
            return min_squares
        return dfs(0)