class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        x = 0 
        y = 0 
        offset = 1
        count = 1
        loop = n//2
        for offset in range(1,loop+1):
            if n == 1:
                nums[x][y] = count
                break
            for i in range(y,n - offset):
                nums[x][i] = count 
                count +=1
            for j in range(x,n-offset):
                nums[j][n- offset] = count 
                count +=1
            for i in range(n- offset,y,-1):
                nums[n-offset][i] = count 
                count += 1
            for j in range(n-offset,x,-1):
                nums[j][y] = count 
                count += 1
            x +=1 
            y +=1
        if  n%2 == 1:
            nums[loop][loop] = count    
        return nums

