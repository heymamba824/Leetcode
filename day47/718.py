class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #dp[i][j]: the length of nums[:i-1] and nums[:j-1]
        size1 = len(nums1)
        size2 = len(nums2)
        dp = [[0] * (size2+1) for _ in range(size1+1)]
        dp[0][0] = 0
        re = 0 
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
                re = max(dp[i][j],re)
        return re 



class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        
        def dfs(n, m):
            if n == len(nums1) or m == len(nums2):
                return 0 
            key = (n, m)
            if key in memo:
                return memo[key]
            if nums1[n] == nums2[m]:
                memo[key] = 1 + dfs(n+1, m+1)
            else:
                memo[key] = 0
            return memo[key]
        
        re = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                length = dfs(i, j)
                re = max(re, length)
        
        return re