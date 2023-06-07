class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        def backtracking(index):
            if len(path) > 1:
                result.append(path[:]) 
            used = set()
            for i in range(index, len(nums)):
                if len(path) > 0 and nums[i] < path[-1] or nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i]) 
                backtracking(i+1)
                path.pop()
        backtracking(0)
        return result


