class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_table = [0] * 26
        left = 0
        right = 0
        re = []
        for i in range(len(s)):
            char_table[ord(s[i])- ord('a')] = i 
        for i in range(len(s)):
            right = max(right,char_table[ord(s[i])- ord('a')]) 
            if i == right:
                re.append(right -left + 1)
                left = right + 1
        return re 