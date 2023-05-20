class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1 
            right = len(nums) - 1  
            if nums[i] > 0 :
                break
            while left < right:
                re = nums[i] + nums[left] + nums[right]
                if re == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and  nums[left] == nums[left+1]:
                        left += 1
                    while left < right and  nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif re > 0 :
                    right -= 1
                else:
                    left += 1
        return result