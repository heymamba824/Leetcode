class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <=1 :
            return intervals
        intervals.sort(key = lambda x: x[0])
        re = [intervals[0]]
        for interval in intervals[1:]:
            last = re[-1]
            if interval[0] <= last[1]:
                last[1] = max(last[1],interval[1])
            else:
                re.append(interval)
        return re