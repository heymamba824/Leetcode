class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        re = 0
        #dp[i][j]:  s[i:j] is palindromic，
        dp = [[False] * size for _ in range(size)]
        for i in range(size-1,-1,-1):
            for j in range(i,size):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        re += 1
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                            re += 1
        return re


class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_pal(left,right):
            res = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            return res
        re = 0 
        n = len(s)
        for i in range(n):
            re += count_pal(i,i)
            re += count_pal(i,i+1)
        return re