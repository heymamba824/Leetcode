class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next(n):
            sum = 0 
            while n:
                sum += (n%10)**2
                n = n//10
            return sum   
        record = set()
        
        while n!= 1 and n not in  record:
            record.add(n)
            n = next(n)
        return n == 1