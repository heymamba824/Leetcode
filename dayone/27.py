class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0 
        fast = 0 
        while fast <= len(nums)-1:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow
