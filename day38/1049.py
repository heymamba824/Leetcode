class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total//2
        #dp[i] = max(dp[i],dp[target - i] + i)
        #dp = [0] *(target+1)
        #dp[0] = stones[0]
        

        memo = {}
        def dfs(n,weight):
            if n == len(stones) or weight >= target:
                return abs(weight * 2 - total)
            key = (n,weight)
            if key in memo:
                return memo[key]
            memo[key] = min(dfs(n+1,weight),dfs(n+1,weight+stones[n]))
            return memo[key]
        return dfs(0,0)