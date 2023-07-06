class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        re = [0] * size
        stack = [0]
        for i in range(1,size):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    index = stack.pop()
                    re[index] = i - index
                stack.append(i)
        return re 
