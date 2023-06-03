class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        path = ''
        result = []
        def backtracking(index):
            nonlocal path
            if len(path) == len(digits):
                result.append(path)
                return 
            digit = mapping[digits[index]]
            for char in digit:
                path += char
                backtracking(index + 1)
                path = path[:-1]

        backtracking(0)
        return result   