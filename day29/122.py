class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        re = 0 
        pro = 0 
        for i in range(1,len(prices)):
            pro = prices[i] - prices[i-1]
            if pro >= 0:
                re += pro
            
        return re 