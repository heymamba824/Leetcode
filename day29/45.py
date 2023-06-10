class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 
        cover = 0 
        time = 0 
        next_cover = 0 
        for i in  range(len(nums)):
            next_cover = max(next_cover,nums[i]+i)
            if i == cover:
                if cover < len(nums) - 1:
                    time += 1
                    cover = next_cover
                if cover >= len(nums) -1 :
                    return time