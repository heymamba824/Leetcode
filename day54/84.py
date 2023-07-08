class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        re = 0 
        heights.insert(0,0)
        heights.append(0)
        stack = [0]
        for i in range(1,len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid = stack.pop()
                    if stack:
                        left = stack[-1]
                        re = max(re, (i-left - 1) * heights[mid])
                        #print(mid,re)
                stack.append(i)
        return re