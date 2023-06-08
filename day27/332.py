class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        used = [0] * len(tickets)
        path = ['JFK']
        result = []
        def backtracking(cur):
            if len(path) == len(tickets) + 1:
                result.append(path[:])
                return True
            for i,ticket in enumerate(tickets):
                if cur == ticket[0] and used[i] == 0:
                    used[i] = 1
                    path.append(ticket[1])
                    state = backtracking(ticket[1])
                    path.pop()
                    used[i] =0 
                    if state:
                        return True
        backtracking('JFK')
        return result[0] 