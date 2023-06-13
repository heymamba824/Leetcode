class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur <0:
                cur = 0 
                start = i + 1
        if total >= 0:
            return start
        else:
            return -1