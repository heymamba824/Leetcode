class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0 
        g.sort()
        s.sort()
        for i in range(len(s)):
            if result < len(g) and s[i] >= g[result]:
                result += 1
        return result   
        