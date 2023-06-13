class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key = lambda x : abs(x),reverse = True)
        for i in range(len(nums)):
            if k > 0 and nums[i] <=0:
                k -= 1
                nums[i] = - nums[i]
        if k>0:
            nums[-1] = nums[-1] * (-1)**(k%2)
        return sum(nums)