class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        def backtracking():
            if len(path) == len(nums):
                result.append(path[:])
                return 
            used = set()
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                used.add(num)
                backtracking()
                path.pop()
        backtracking()
        return result 


