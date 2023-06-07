class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        nums.sort()
        use = [0] * len(nums)
        def backtracking():
            if len(path) == len(nums):
                result.append(path[:])
                return
            #used = set()
            for i in range(len(nums)):
                if i>0 and nums[i]== nums[i-1] and use[i-1] == 0:
                    continue
                if use[i] == 1:
                    continue
                #if nums[i] in used:
                #    continue
                #used.add(nums[i])
                use[i] = 1
                path.append(nums[i])
                backtracking()
                use[i] = 0
                path.pop()
        backtracking()
        return result 