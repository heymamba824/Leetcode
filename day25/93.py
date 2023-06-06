class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(s):
            if 0<len(s)<=3 and 0<= int(s)<= 255 and str(int(s)) == s:
                return True
            else:
                return False 
        
        path = [ ]
        result = [ ]
        def backtracking(index,count):
            if count == 4 and index == len(s):
                result.append('.'.join(path))
                return 
            
            for i in range(index,index +3):
                if i <= len(s):
                    temp = s[index:i+1]
                    #print(temp)
                    if is_valid(temp):
                        path.append(temp)
                        backtracking(i + 1,count+1)
                        path.pop()        
                    else:
                        break 
                else:
                    break 
        backtracking(0,0)
        return result 