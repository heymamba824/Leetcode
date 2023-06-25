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