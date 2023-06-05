class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        def backtracking(index):
            if len(s) == index:
                result.append(path[:])
                return 
            for i in range(index,len(s)):
                temp = s[index:i + 1]
                if temp == temp[::-1]:
                    path.append(temp)
                else:
                    continue
                backtracking(i+1)
                path.pop()
        backtracking(0)
        return result