class Solution:
    def reverseWords(self, s: str) -> str:
        def space(s):
            n = len(s)
            left = 0 
            right = n -1 
            while left <=right and s[left] == ' ':
                left +=1
            while left <=right and s[right] == ' ':
                right -=1 
            trans = []
            while left <= right:
                if s[left] != ' ':
                    trans.append(s[left])
                elif s[left] == ' ' and s[left-1] != ' ':
                    trans.append(s[left])
                left += 1
            return trans
        
        def revereall(s):
            left = 0 
            right = len(s) -1 
            while left < right:
                s[left],s[right] = s[right],s[left]
                left +=1
                right -=1
            return s

        def reverepic(s):
            left = 0
            right = 0
            while right<len(s):
                if s[right] == ' ':
                    s[left:right] = revereall(s[left:right])
                    left = right + 1
                right +=1
            s[left:len(s)] = revereall(s[left:len(s)])
            return ''.join(s)

        s = space(s)
        s = revereall(s)
        s = reverepic(s)
        return s 
        
