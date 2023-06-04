class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        pivot = n//2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        first_index = 0 
        second_index = 0 
        res = []
        while first_index < len(left) and second_index < len(right):
            if left[first_index] < right[second_index]:
                res.append(left[first_index])
                first_index += 1
            else:
                res.append(right[second_index])
                second_index += 1

        res += left[first_index:]
        res += right[second_index:]
        return res     