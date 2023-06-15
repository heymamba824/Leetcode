class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        #1234
        #4321 3999
        #109 99  i = 0 
        s = list(str(n))
        for i in range(len(s)-2,-1,-1):
            if s[i] > s[i+1]:
                #print(i,s[i])
                s[i] = str(int(s[i])-1)
                s[i+1:] = '9'*(len(s)-i-1)
        return int(''.join(s))