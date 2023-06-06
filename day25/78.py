class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        def backtracking(index):
            result.append(path[:])
            for i in range(index,len(nums)):
                path.append(nums[i])
                backtracking(i+1)
                path.pop()
        backtracking(0)
        return result 