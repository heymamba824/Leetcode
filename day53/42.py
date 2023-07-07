class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        stack = [0]
        re = 0
        for i in range(1,len(height)):
            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid = stack.pop()
                    if stack:
                        left = stack[-1]
                        re += (min(height[left],height[i]) - height[mid]) * (i-left-1)
                stack.append(i)
        return re