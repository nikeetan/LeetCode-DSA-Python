'''
i would apply the bfs on the neighbors and find the maximum gain and proceed with that gai
'''
from collections import deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u] = [v]
            elif u in adj:
                adj[u].append(v)
            if v not in adj:
                adj[v] = [u]
            elif v in adj:
                adj[v].append(u)

        bobpath = {}
        visited = set()
        time = 0
        def findbobpath(sourceNode, time):
            bobpath[sourceNode] = time
            visited.add(sourceNode)
            if sourceNode == 0:
                return True
            for nei in adj.get(sourceNode, []):
                if nei not in visited:
                    if findbobpath(nei, time + 1):
                        return True 
            bobpath.pop(sourceNode)
            return False
        findbobpath(bob, 0)
        maxIncome = float('-inf')
       
        #start, time, cost
        start = (0, 0, 0)
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(0)
        while queue:
            node, time, income = queue.popleft()
            if (node not in bobpath)or (bobpath[node] > time):
                income += amount[node]
            elif bobpath[node] == time:
                income += (amount[node]) // 2
            if (len(adj[node]) == 1) and (node != 0):
                maxIncome = max(maxIncome, income)

            for nei in adj.get(node, []):
                if nei not in visited:
                    queue.append((nei, time + 1, income))
                    visited.add(nei)

        return maxIncome
                





