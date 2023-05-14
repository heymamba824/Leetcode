def helper(nums):
            size = len(nums)
            if size == 1:
                return nums[0]
            dp = [0]* size
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,size):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        
        if len(nums)==1:
            return nums[0]
        return max(helper(nums[1:]),helper(nums[:-1]))