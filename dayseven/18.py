class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        re = []
        for i in range(n):
            if nums[i]>target and target >0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if nums[i] + nums[j] >target and target>0:
                    break
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n-1
                while left < right:
                    res = nums[i] + nums[j] + nums[left] + nums[right]
                    if res > target:
                        right -=1
                    elif res < target:
                        left +=1
                    else:
                        re.append([nums[i],nums[j],nums[left],nums[right]])    
                        while left<right and nums[right -1] == nums[right]:
                            right -=1
                        while left < right and nums[left] == nums[left+1]:
                            left +=1
                        right -= 1 
                        left += 1
        return re