class Solution:
    def candy(self, ratings: List[int]) -> int:
        #left to right 
        size = len(ratings)
        re = [1] * size
        for i in range(1,size):
            if ratings[i] > ratings[i-1]:
                re[i] = re[i-1] + 1
        for i in range(size - 2,-1,-1):
            if ratings[i] > ratings[i+1]:
                re[i] = max(re[i],re[i+1] + 1)
        return sum(re)