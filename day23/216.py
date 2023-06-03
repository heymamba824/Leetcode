class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = [ ]
        def backtracking(index,total):
            if total == n and len(path) == k:
                result.append(path[:])
                return 

            end_index =  11 - (k-len(path))  
            for i in range(index,end_index):
                if total + i > n:
                    break
                else:
                    path.append(i)
                    backtracking(i+1,total + i)
                    path.pop()
        backtracking(1,0)
        return result