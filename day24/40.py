class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = [ ]
        result = [ ]
        candidates.sort()
        used = [0] * len(candidates)
        def backtracking(index,total):
            if total == target:
                result.append(path[:])
                return
            for i in range(index,len(candidates)):
                if candidates[i] + total > target:
                    return 
                if i > 0 and candidates[i] == candidates[i-1] and used[i-1] == 0:
                    continue 
                path.append(candidates[i])
                used[i] = 1 
                backtracking(i + 1,candidates[i] + total)
                used[i] = 0 
                path.pop()
        backtracking(0,0)
        return result 



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = [ ]
        result = [ ]
        candidates.sort()
        def backtracking(index,total):
            if total == target:
                result.append(path[:])
                return
            for i in range(index,len(candidates)):
                if candidates[i] + total > target:
                    return 
                if i > index and candidates[i] == candidates[i-1]:
                    continue 
                path.append(candidates[i])
                backtracking(i + 1,candidates[i] + total)
                path.pop()
        backtracking(0,0)
        return result 