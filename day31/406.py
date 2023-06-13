class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0],x[1]))
        re = []
        for p in people:
            re.insert(p[1],p)
        return re