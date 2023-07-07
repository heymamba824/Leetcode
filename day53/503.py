class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums *= 2
        size = len(nums)
        re  = [-1] * size
        stack = [0]
        for i in range(1,size):
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i] > nums[stack[-1]]:
                    index = stack.pop()
                    re[index] = nums[i]
                stack.append(i)
        return re[:size//2]