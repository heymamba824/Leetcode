class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        candidates.sort()
        def backtracking(total,index):
            if total == target:
                result.append(path[:])
                return 
            for i in range(index,len(candidates)):
                if total + candidates[i] > target:
                    return
                total += candidates[i]
                path.append(candidates[i])
                backtracking(total,i)
                total -= candidates[i]
                path.pop()
        backtracking(0,0)
        return result