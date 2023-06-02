class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [ ]
        path = [ ]
        def backtracking(index):
            if len(path) == k:
                result.append(path[:])
                return 
            for i in range(index,n+1):
                path.append(i)
                backtracking(i + 1)
                path.pop()
        backtracking(1)
        return result 