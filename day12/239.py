class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que = deque()
        result = []
        for i in range(k):
            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
        result.append(que[0])
        for i in range(k,len(nums)):
            if nums[i -k] == que[0]:
                que.popleft()
            while que and  nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
            result.append(que[0])
        return result 



class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que = deque()
        result = []
        for i in range(len(nums)):
            if i>=k and nums[i-k] == que[0]:
                que.popleft()

            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
            if i >= k-1:
                result.append(que[0])
        return result  