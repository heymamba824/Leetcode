class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess = ['.' * n for _ in range(n)]
        result = []

        def is_valid(row,col):
            for i in range(row):
                #print("####")
                #print(i,col)
                #print(chess[i][col])
                if chess[i][col] == 'Q':
                    return False
            i = row - 1 
            j = col - 1
            while i>=0 and j>=0:
                if chess[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i = row - 1
            j = col + 1 
            while i>=0 and j<n:
                if chess[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
        
        def backtracking(row):
            if row == n:
                result.append(chess[:])
                return 
            for col in range(n):
                #print(n,row,col)
                if is_valid(row,col):
                    chess[row] = chess[row][:col] + 'Q' + chess[row][col+1:]
                    backtracking(row + 1)
                    chess[row] = chess[row][:col] + '.' + chess[row][col+1:]
        backtracking(0)
        return [[''.join(row) for row in solution] for solution in result]
            