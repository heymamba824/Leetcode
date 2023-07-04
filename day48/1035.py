class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        dp = [[0] * (size2+1) for _ in range(size1+1)]
        re = 0 
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
                re = max(re,dp[i][j])
        return re