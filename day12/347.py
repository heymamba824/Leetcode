class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        result = []
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        for val,time in dic.items():
            if len(result) == k:
                if time > result[0][0]:
                    heapq.heappop(result)
                    heapq.heappush(result,(time,val))
            else:
                heapq.heappush(result,(time,val))
        return [i[1] for i in result]