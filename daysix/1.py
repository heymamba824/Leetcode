class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            re = target - nums[i]
            if re in dic:
                return [i,dic[re]]
            dic[nums[i]] = i 