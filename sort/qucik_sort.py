1.二路划分，对于等于的部分也进行交换


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def findmid(nums,left,right):
            temp = nums[left]
            while left < right:
                while nums[right] >= temp and left < right:
                    right -= 1
                nums[left] = nums[right]
                while nums[left] <= temp and left < right:
                    left += 1
                nums[right] = nums[left] 

            nums[left] = temp
            return left
        def quick_sort(nums,left,right):
            if left < right:
                mid = findmid(nums,left,right)
                quick_sort(nums,left,mid - 1)
                quick_sort(nums,mid+1,right)
        quick_sort(nums,0,len(nums)-1)
        return nums


2.三路划分，速度更快

